from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import json
import webbrowser
import time
import sys


json_data = json.load(open("/home/pi/2019-ca400-randlea2/src/command_scripts/control_youtube/screen_positions.json", "r"))
mouse_controller = MouseController()
keyboard_controller = KeyboardController()


def search_youtube(search_term):
    click_position("search bar")
    type_sentence(search_term)
    click_position("search button")
    return None


def click_position(position_name):
    data = json_data[position_name]
    position = (data[0], data[1])
    click_screen_position(position)
    return None


def clear_text():
    click_position("search bar")
    keyboard_controller.press(Key.backspace)
    time.sleep(2)
    keyboard_controller.release(Key.backspace)


def click_first_result():
    click_position("first result")


def click_second_result():
    click_position("second result")


def click_third_result():
    click_position("third result")


def open_browser(url):
    webbrowser.open(url)


def remove_stop_words(spoken_words):
    stop_words = ["for", "search", "youtube", "a"]
    removed = [word for word in spoken_words if word not in stop_words]
    new_search_string = " ".join(removed)
    return new_search_string


def type_sentence(sentence):
    for char in sentence:
        keyboard_controller.press(char)
        keyboard_controller.release(char)


def click_screen_position(xy):
    x = xy[0]
    y = xy[1]
    mouse_controller.position = (x, y)
    mouse_controller.click(Button.left, 1)


def main(spoken_words):
    # open_browser("https://www.youtube.com/")
    clear_text()
    search_query = remove_stop_words(spoken_words)
    if search_query != "":
        search_youtube(search_query)
        time.sleep(3)
        click_first_result()


if __name__ == "__main__":
    main(sys.argv[1])