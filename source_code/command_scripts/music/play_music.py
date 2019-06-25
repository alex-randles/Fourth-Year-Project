import urllib
import requests
import os
import sys
import subprocess
import pafy
import sqlite3
import random
from bs4 import BeautifulSoup
import requests

#custom modules
import hotword
import speak

# database previously searched songs
database = "/home/pi/2019-ca400-randlea2/src/command_scripts/music/songs.db"


def play_song(song_name):
    playlist_keywords = ['shuffle', 'playlist']
    # check if there are activating playlist
    if set(playlist_keywords).issubset(set(song_name.strip().split())):
        speak.speak_to_user("shuffling playlist")
        print("playlist starting")
        shuffle_playlist()
    elif get_song_details(song_name) is None:
        speak.speak_to_user("searching for song")
        url = create_youtube_url(song_name)
        youtube_url = get_first_result(url)
        song_url, song_title = get_song(youtube_url)
        # add song details to database for further searches
        add_song_details(song_name,song_title, youtube_url, song_url)
        play_url(song_url)
    else:
        # song in database, retrieve song url and play it
        song_url = get_song_url(song_name)
        play_url(song_url)


def create_youtube_url(search_term):
    # create youtube url to search results list
    youtube_url = "https://www.youtube.com/results?search_query="
    search_term = search_term.split(" ")
    search_term = "+".join(search_term)
    print(search_term)
    youtube_url += search_term
    print(youtube_url)
    return youtube_url




def remove_db_entry(song_url):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM songs WHERE song_url=?", (song_url,))



def get_first_result(url):
    # retrieves the search results list and gets first result url
    html = requests.get(url).text
    parser = BeautifulSoup(html, 'html.parser')
    results = parser.findAll(attrs={'class': 'yt-uix-tile-link'})
    first_result = "https://www.youtube.com" + results[0]["href"]
    print(first_result)
    return first_result


def get_song(url):
    song = pafy.new(url)
    # find best audio stream
    audiostreams = song.audiostreams
    best_audio_stream = audiostreams[0].url
    song_title = song.title
    return best_audio_stream, song_title


def play_url(url):
    # start hotword in background & play the song
    subprocess.Popen(["python3", "/home/pi/2019-ca400-randlea2/src/hotword.py","&"])
    subprocess.call(["mplayer", url])


def create_table():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # database only needs to be created once
        cursor.execute(""" CREATE TABLE IF NOT EXISTS songs (
          song_name text primary key,
          song_title text,
          youtube_url text,
          song_url text
            )""")


def add_song_details(song_name, song_title, youtube_url, song_url):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # add if not in database
        cursor.execute("INSERT OR IGNORE INTO songs (song_name, song_title, youtube_url, song_url) VALUES (?, ?, ?, ?)",(song_name, song_title, youtube_url, song_url))
        print("{} added successfully".format(song_name))

def get_song_details(song_name):
    # look for song details
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        ## check if song in database
        cursor.execute("SELECT * from songs where song_name = ?", (song_name,))
        result = cursor.fetchone()
        print(result)
    return result


def get_song_url(song_name):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # check if song in database and retrieve song url
        cursor.execute("SELECT * FROM songs where song_name = ?",(song_name,))
        result = cursor.fetchone()
    # return none if not in database
    if result is not None:
        return result[3]
    return result


def get_youtube_url(song_name):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # check if song in database and retrieve song url
        cursor.execute("SELECT youtube_url FROM songs_url WHERE song_name = ?",(song_name,))
        result = cursor.fetchone()
    # return none if not in database
    if result is not None:
        return result[0]
    return result


def get_song_name():
    speak.speak_to_user("what song would you like to play")
    song_name = convert_speech_to_text()
    split_song_name = song_name.split(" ")
    return split_song_name


def shuffle_playlist():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        # retrieve all previously searched songs
        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()
        if len(songs) > 0:
            random_song = random.choice(songs)
            while len(songs) >= 1:
                song_name, song_url = random_song[1], random_song[3]
                # ensure a valid url is provided
                speak.speak_to_user("playing {}".format(song_name))
                play_url(song_url)
                # remove songs that have been played
                songs.remove(random_song)
                random_song = random.choice(songs)
        else:
            speak.speak_to_user("No songs currently in your playlist")
            hotword.detect_hotword()
        return None


def parse_user_input(spoken_words):
    print(spoken_words)
    if "playlist" not in spoken_words:
        # remove these words from search string
        excluded_words = ["play"]
        new_spoken_words = [word for word in spoken_words if word not in excluded_words]
        string_spoken_words = " ".join(new_spoken_words)
        return string_spoken_words
    string_spoken_words = " ".join(spoken_words)
    return string_spoken_words


def main(spoken_words):
    create_table()
    song_name = parse_user_input(spoken_words)
    print(song_name)
    play_song(song_name)

if __name__ == "__main__":
    main(sys.argv[1:])

