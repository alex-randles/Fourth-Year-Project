# new command recogniser
# previous layout was inadequate
# import files from other directories
# sys.path.insert(0, 'path/to/your/py_file')

import os, time, sys, os, sqlite3, pyaudio, wave, array, speech_recognition, signal, difflib, subprocess
from listening_leds import listening_leds
from speaking_leds import speaking_leds
import search_information_v3

# databases
command_db = "command_database.db"
security_db = "security.db"


def query_user():
    print(time.time())
    listening_leds()
    create_command_table()
    create_security_table()
    add_all_commands()
    # used for testing when I  cant speak to system
    if sys.argv[1:] == []:
        spoken_words = translate_audio()
    else:
        spoken_words = " ".join(sys.argv[1:])
    command = find_command(spoken_words)
    if command is not None:
        command_script = find_script_location(command)
        print(command_script)
        run_script(command_script, command, spoken_words)
    else:
        speak("command not found")
        subprocess.call(["python3 /home/pi/2019-ca400-randlea2/src/hotword.py"], shell=True)


# return the current hotword settings e.g snowboy.pmdl or snowboy.udml
def create_security_table():
    # create the security table if not already
    with sqlite3.connect(security_db) as connection:
        cursor = connection.cursor()
        cursor.execute(""" CREATE TABLE if NOT EXISTS security(
		security_lock text primary key,
		hotword_file  text
          )""")
        # set initial security level
        cursor.execute("INSERT or IGNORE INTO security(security_lock,hotword_file)values(?,?) ",
                       ("false", "snowboy.umdl",))
        cursor.execute("SELECT * FROM security")
        results = cursor.fetchone()
        print(results)
    return results[1]


## if the user wishes to change the security, this function will be called
def change_security():
    speak("would you like to turn security on or off")
    ## this is whether they'd like to turn on or turn off
    # spoken_words  = translate_audio()
    # split_words = spoken_words.strip().split()[0]
    split_words = ["turn", "security", "off"]
    if "on" in split_words:
        request_level = "true"
    elif "off" in split_words:
        request_level = "false"
    with sqlite3.connect(security_db).cursor() as cursor:
        # delete the current settings
        cursor.execute("DELETE from security")
        hotword_levels = {"true": "snowboy.pmdl", "false": "snowboy.umdl"}
        cursor.execute("INSERT or IGNORE into security(security_lock,hotword_file)values(?,?) ",
                       (request_level, hotword_levels[request_level],))
        cursor.execute("SELECT * from security")
        results = cursor.fetchall()
        print(results)
        speak("security settings successfully changed")


def start_connection(db_file):
    try:
        ## connect to database
        print("connection success")
        create_command_table()



    ## unable to connect to database
    except sqlite3.Error as error:
        print(error)


def create_command_table():
    ## database only needs to be created once
    ## command keywords can't be stored as list, ["play","music"]
    ## must be stored as string which i can use .split(" ") on i.e "play music".split(" ") = ["play","music"]
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
    ##				(command_name,command_key_words,script_location,require_command_line,activation_speech)
    ## command keywords must be stored as string with whitespace then split as sql cannot store list
    command_scripts = [("joke", "joke", "joke/jokes.py", "false", "telling a joke	"),
                       ("send_email", "send email", "email/send_email_v2.py", "true", ""),
                       ("read_email", "read email", "email/read_unread_email.py", "false", ""),
                       ("time", "time", "time/time.py", "false", "telling the time		"),
                       ("news", "news", "news/get_news_v2.py", "false",
                        "the news headlines for today are		"),
                       ("security", "change security",
                        "from commandRecogniserV16 import changeSecurity; changeSecurity()", "false", ""),
                       ("music", "play music", "music/play_music_v6.py", "false", ""),
                       ("search", "what is", "search_information/search_information_v3.py", "true",
                        "searching for information"),
                       ("test", "turn off", "tv/turn_off.py", "false", ""),
                       ("test_2", "turn on", "tv/turn_on.py", "false", ""),
                       ("translator", "translate", "translation/translate_v6.py", "false", ""),
                       ("pause_song", "pause song", "hotword.py", "false", ""),
                       ("play_song", "play song", "music/play_song.py", "", "false"),
                       ("stop_song", "stop song", "music/stop_song.py", "", "false")
                       ]
    # add all commands in command scripts list into database
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        for command_details in command_scripts:
            add_command(command_details[0], command_details[1], command_details[2], command_details[3],
                        command_details[4])


def add_command(command, command_key_words, script_location, require_command_line, activation_speech):
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        # add if not already
        cursor.execute(
            "INSERT OR IGNORE INTO commands ( 'command', 'command_key_words', 'script_location', 'require_command_line', 'activation_speech') VALUES (?, ?, ?, ?, ?)",
            (command, command_key_words, script_location, require_command_line, activation_speech))
        success_output = "the command {} has been added successfully".format(command)


def find_command(spoken_words):
    # find the correct script user wants to activate
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        # add if not in database
        cursor.execute("SELECT * from commands")
        results = cursor.fetchall()
        all_command_key_words = []
        for command in results:
            command_key_words = command[1].split()
            spoken_key_words = spoken_words.split()
            # string for closest match
            all_command_key_words.append(" ".join(command_key_words))
            if set(command_key_words).issubset(set(spoken_key_words)):
                return command
        # if command is not returned
        print(spoken_words, all_command_key_words)
        closest_match = difflib.get_close_matches(spoken_words, all_command_key_words)
        closest_key_words = closest_match[0]
        # return closest matching command
        match_command = cursor.execute("SELECT * FROM commands WHERE  command_key_words=?", (closest_key_words,))
        return match_command.fetchone()

    return None


def speak_activation_sentence(command):
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT activation_speech FROM commands where command=?", (command[0],))
        activation_sentence = cursor.fetchone()[0]
        if activation_sentence != "":
            speak(activation_sentence, background=True)
            print("speaking activation sentence")
        else:
            print("not speaking activation sentence")


def speak(sentence):
    # runs the pico2wave speaking script
    subprocess.call(["$HOME/2019-ca400-randlea2/src/speakText.sh 'The time is {}".format(sentence)], shell=True)


def match_key_words(command_key_words):
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        spoken_words = translate_speech()
        cursor.execute("SELECT * FROM commands")
        results = cursor.fetchall()
        for command in results:
            command_key_words = command[1]
            if set(spoken_words).issubset(command_key_words):
                return command

    return None


def requires_arguments(command):
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        print(command)
        cursor.execute("SELECT require_command_line FROM commands WHERE command=?", (command[0],))
        result = cursor.fetchone()[0]
        return result


def run_script(command_script, command, spoken_words):
    # check if requires command line arguments
    # script_dir = "/".join(command_script.strip().split("/")[3:-1])
    # os.chdir(script_dir)
    check = requires_arguments(command)
    speak_activation_sentence(command)
    print(command)
    if command[0] == "pause_song":
        subprocess.call(["python3 {}".format("$HOME/2019-ca400-randlea2/src/hotword.py")], shell=True)
    elif check == "true":
        subprocess.call(["python3 {} {}".format(command_script, spoken_words)], shell=True)
    else:
        subprocess.call(['python3', "/"+ command_script])
        # subprocess.call(["python3 {}".format(command_script)], shell=True)


## get the locaiton of corresponding command script
def find_script_location(command):
    ## get command name out of command database entry
    command_name = command[0]
    ## look for command script
    with sqlite3.connect(command_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT  script_location FROM commands where command = ?", (command_name,))
        result = cursor.fetchone()
        print(result[0])
    ## all scripts stored in same subfolder _ command_scripts
    script_location = "$HOME/2019-ca400-randlea2/src/command_scripts/{}".format(result[0])
    return script_location


## match user spoken words with command key words (hopefully)
def command_name(spoken_words):
    with sqlite3.connect(command_db).cursor() as cursor:
        cusor.execute("SELECT command_key_words FROM commands")
        result = command_cursor.fetchall()
    return result[0]


def translate_speech():
    text = translate_audio()
    return text


def get_command_name(command):
    return command[0]


# led configuration for speaking (all white) & runs script for speaking
def speak(sentence, background=False):
    if background is True:
        subprocess.call(["/home/pi/2019-ca400-randlea2/src/speakText.sh",sentence + "&"])
    else:
        subprocess.call(["$HOME/2019-ca400-randlea2/src/speakText.sh '{}'".format(sentence)])


#################################
###   speech recognition ########
#################################


def record_audio():
    ## start pyaudio
    audio = pyaudio.PyAudio()
    audio_stream = audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)
    # input_device_index = 3)
    return audio, audio_stream


def detect_audio(audio_stream):
    # maximum length of silence
    max_silence = 43
    silent_counter = 0
    # minimum length of recording
    min_time = 100
    time_counter = 0
    ## level it must reach to start recording
    volume_threshold = 200
    # has a word been deteced
    words_spoken = False
    data_container = []
    # while silence is not greater than 1 second
    while silent_counter < max_silence and time_counter < min_time:
        ## start taking in data
        data = audio_stream.read(1024, exception_on_overflow=False)
        data_chunk = array.array('h', data)
        sound_level = max(data_chunk)
        ## threshold for silence
        print(sound_level)
        if sound_level > volume_threshold:
            words_spoken = True
            data_container.append(data)
        elif words_spoken is True:
            if len(data_container) > 10:
                silent_counter += 1
        time_counter += 1
    return audio_stream, data_container


def write_audio(file_name, audio_stream, audio, data_container):
    ## get non silent recording
    # audio_stream = detect_audio()
    # stop recording
    terminate(audio_stream)
    ## get pyaudio
    # audio = record_audio()
    audio.terminate()
    # writing to file
    audio_file = wave.open(file_name, 'wb')
    ## set paramaters
    audio_file.setnchannels(2)
    audio_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(44100)
    ## add frames to the file
    audio_file.writeframes(b''.join(data_container))
    terminate


def terminate(audio_stream):
    ## close the audio stream
    audio_stream.stop_stream()
    audio_stream.close()


def translate_audio():
    ## location of audio file
    audio_file = "speech.wav"
    ## start pyaudio
    audio, audio_stream = record_audio()
    ## get the audio
    new_audio_stream, data_container = detect_audio(audio_stream)
    ## wite the audio to a file
    write_audio(audio_file, new_audio_stream, audio, data_container)
    ## translate the audio file to  text
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print(text.lower())
        return text.lower()


def translate_audio():
    ## location of audio file
    audio_file = "speech.wav"
    ## start pyaudio
    audio, audio_stream = record_audio()
    ## get the audio
    new_audio_stream, data_container = detect_audio(audio_stream)
    ## wite the audio to a file
    write_audio(audio_file, new_audio_stream, audio, data_container)
    ## translate the audio file to  text
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print(text.lower())
        return text.lower()


if __name__ == "__main__":
    query_user()
