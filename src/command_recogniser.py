import os
import time
import sys
import sqlite3
import difflib
import subprocess

# custom modules
# added all them to python path in bottom line of ~/.bashrc
import command_scripts
import translate_speech
import speaking_leds
import hotword
import importlib
import speak

# database
command_db = "/home/pi/2019-ca400-randlea2/src/commands.db"


def query_user():
        speaking_leds.speaking_leds()
        subprocess.call(["/home/pi/2019-ca400-randlea2/src/stop_arecord.sh"])
        spoken_words = translate_speech.start_translator()
        create_command_table()
        add_all_commands()
        command = find_matched_keywords(spoken_words)
        # find command if words spoken otherwise do nothing
        if spoken_words  == "":
            hotword.detect_hotword()
        elif command is not None:
            command_script = find_module_location(command)
            print(command_script)
            run_script(command_script, command, spoken_words)
        else:
            speak.speak_to_user ("command not found")
            hotword.detect_hotword()
    #except:
     #   speak.speak_to_user("problem with command, try again")
      #  hotword.detect_hotword()


def create_command_table():
    # sqlite doesnt support list directly so 'I used a string
    # must be stored as string which i can use .split(" ") on i.e "play music".split(" ") = ["play","music"]
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS commands (
		  command text primary key,
		  command_key_words text,
		  script_location text,
		  require_command_line text,
		  activation_speech text 
		  )""")
        print("commands table created successfully!")


def add_all_commands():
    # command keywords must be stored as string with whitespace then split as sql cannot store list
    #				(command_name,command_key_words,module location,require_command_line?,activation_speech)
    command_scripts = [("joke", "joke", "joke.jokes", "false", ""),
                       ("send_email", "send email", "emails.send_email", "true", ""),
                       ("read_email", "read email", "emails.read_unread_email", "false", ""),
                       ("time", "time", "time.get_time", "false", ""),
                       ("help", "help", "help.get_help", "false", ""),
                       ("news", "news", "news.get_news", "false", ""),
                       ("sports", "sports", "sports.get_sports", "false", ""),
                       ("weather", "weather", "weather.get_weather", "false", ""),
                       ("security", "security", "security.change_security", "true", ""),
                       ("search_info", "what is", "search_information.search_wiki", "true",""),
                       ("search_person", "who", "search_information.search_wiki", "true",""),
                       ("control_candle", "candle", "tv.send_ir_signal", "true", ""),
                       ("record_signal", "record", "tv.record_ir_signal", "false", ""),
                       ("pair_device", "pair", "smart_plug.pair_device", "false", ""),
                       ("control_plug", "plug", "smart_plug.control_plug", "true", ""),
                       ("translator", "translate", "translation.translate_language", "true", ""),
                       ("play_music", "play", "music.play_music", "true", "searching for song"),
                       ("pause_song","pause song", "hotword", "false", ""),
                       ("play_song", "play song", "music.resume_song", "false" , ""),
                       ("stop_song", "stop song", "music.stop_song", "false", ""),
                       ("shuffle_playlist", "shuffle playlist", "music.play_music", "true", ""),
                       ("youtube_home", "home", "control_youtube.control_youtube", "true", ""),
                       ("youtube_search", "search", "control_youtube.control_youtube", "true", ""),
                       ("youtube_full_screen", "full screen", "control_youtube.control_youtube", "true", ""),
                       ("youtube_small_screen", "small screen", "control_youtube.control_youtube", "true", ""),
                       ("youtube_pause", "pause video", "control_youtube.control_youtube", "true", ""),
                       ("youtube_play", "play video", "control_youtube.control_youtube", "true", ""),
                       ("reload_page", "reload", "control_youtube.control_youtube", "true", ""),
                       ("go_back_or_forward", "go", "control_youtube.control_youtube", "true", ""),
                       ("youtube_first_result", "first result", "control_youtube.control_youtube", "true", ""),
                       ("youtube_second_result", "second result", "control_youtube.control_youtube", "true", ""),
                       ("youtube_third_result", "third result", "control_youtube.control_youtube", "true", ""),
                       ("youtube_third_result", "mute", "control_youtube.control_youtube", "true", ""),

                       ]

    for command_details in command_scripts:
        add_command(command_details[0], command_details[1], command_details[2], command_details[3],
                        command_details[4])
    return None


def add_command(command, command_key_words, script_location, require_command_line, activation_speech):
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        # add if not already
        cursor.execute(
            "INSERT OR IGNORE INTO commands ( 'command', 'command_key_words', 'script_location', 'require_command_line', 'activation_speech') VALUES (?, ?, ?, ?, ?)",
            (command, command_key_words, script_location, require_command_line, activation_speech))
    return None

def find_matched_keywords(spoken_words):
    # find the correct script user wants to activate
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        # add if not in database
        cursor.execute("SELECT * from commands")
        results = cursor.fetchall()
        all_command_key_words = []
        matches = []
        for command in results:
            command_key_words = command[1].split()
            spoken_key_words = spoken_words.split()
            # string for closest match
            all_command_key_words.append(" ".join(command_key_words)) 
            if set(command_key_words).issubset(set(spoken_key_words)):
                    matches.append((command, command_key_words))
        print(matches)
        print("matches")
        # if commands with similar keywords
        if matches:
            return find_closest_match(matches)
        return None


def find_closest_match(matches):
    # find match thats closest
    best_match = max(matches, key=lambda x: x[1])
    print("best match", best_match)
    best_keywords = get_command_key_words(best_match)
    # all other commands take precedent over search information command
    if best_keywords == ["what", "is"]:
        for match in matches:
            current_keywords =  get_command_key_words(match)
            if current_keywords != ["what", "is"]:
                return match[0]
    return best_match[0]


def speak_activation_sentence(command):
    # if there is a an activation sentence speak it
    # general an activation sentence for commands that take a long time to execute
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT activation_speech FROM commands where command=?", (command[0],))
        activation_sentence = cursor.fetchone()[0]
        if activation_sentence != "":
            speak.speak_to_user (activation_sentence, background=True)
            print("speaking activation sentence")
        else:
            print("not speaking activation sentence")
    return None



def requires_arguments(command):
    # some commands require the users speech as an argument
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        print(command)
        cursor.execute("SELECT require_command_line FROM commands WHERE command=?", (command[0],))
        result = cursor.fetchone()[0]
        return result


def run_script(module_name, command, spoken_words):
    # check if  arguments
    check = requires_arguments(command)
    speak_activation_sentence(command)
    print(command)
    if "." not in module_name :
        command_module = importlib.import_module(module_name)
    else:
        command_module = importlib.import_module("command_scripts." + module_name)
    if check == "true":
        spoken_words = spoken_words.strip().split()
        command_module.main(spoken_words)
    else:
        command_module.main()
    return None



def find_module_location(command):
    command_name = get_command_name(command)
    # look for command script
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT  script_location FROM commands where command = ?", (command_name,))
        result = cursor.fetchone()
    return result[0]


def command_name(spoken_words):
    with sqlite3.connect(command_db).cursor() as cursor:
        cusor.execute("SELECT command_key_words FROM commands")
        result = command_cursor.fetchall()
    return result[0]


def get_command_name(command):
    return command[0]

def get_command_key_words(command):
    return command[1]

if __name__ == "__main__":
    query_user()
