import sqlite3

# custom modules
import speak
import hotword

security_db = "/home/pi/2019-ca400-randlea2/src/security.db"

def change_security(spoken_words):
    # check if user wants to turn security on or off
    if "on" in spoken_words:
        request_level = "true"
    elif "off" in spoken_words:
        request_level = "false"
    with sqlite3.connect(security_db) as connection:
        cursor = connection.cursor()
        # delete the current settings
        cursor.execute("DELETE from security")
        hotword_levels = {"true": "snowboy.pmdl", "false": "snowboy.umdl"}
        cursor.execute("INSERT or IGNORE into security(security_lock,hotword_file)values(?,?) ",
                       (request_level, hotword_levels[request_level],))
        cursor.execute("SELECT * from security")
        results = cursor.fetchall()
        print(results)
        speak.speak_to_user("security settings successfully changed")
    return None


# tell the user if security is turned on or not
def check_security():
    # connection to database which stores all security information
    with sqlite3.connect(security_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM security")
        # return the universal or personal model depending on settings
        hotword_file = cursor.fetchall()[0][1]
        if hotword_file == "snowboy.pmdl":
            speak.speak_to_user("security setting is currently on")
        else:
            speak.speak_to_user("security setting is currently off")
        return None


def main(spoken_words):
    if "check" in spoken_words:
        check_security()
    else:
        change_security(spoken_words)
    hotword.detect_hotword()
