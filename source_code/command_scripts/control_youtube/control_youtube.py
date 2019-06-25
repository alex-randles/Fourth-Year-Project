from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import json
import webbrowser
import time
import sys
import hotword

json_data = json.load(open("/home/pi/2019-ca400-randlea2/src/command_scripts/control_youtube/screen_positions.json", "r"))
mouse_controller = MouseController()
keyboard_controller = KeyboardController()


def enter_search_term(search_term):
    keyboard_controller.press("/")
    keyboard_controller.release("/")
    clear_text()
    type_sentence(search_term)
    keyboard_controller.press(Key.enter)
    keyboard_controller.release(Key.enter)
    return None


def click_position(position_name):
    data = json_data[position_name]
    position = (data[0], data[1])
    click_screen_position(position)
    return None


def clear_text():
    click_position("search bar")
    keyboard_controller.press(Key.backspace)
    time.sleep(3)
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
    print(spoken_words)
    stop_words = ["for", "search", "youtube", "a"]
    # removed = [word for word in spoken_words if word not in stop_words]
    for word in stop_words:
        print(word)
        if word in spoken_words:
            spoken_words.remove(word)
            print("word removed" + word)
    new_search_string = " ".join(spoken_words)
    print(new_search_string)
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


def search_youtube(spoken_words):
    # open_browser("https://www.youtube.com/")
    search_query = remove_stop_words(spoken_words)
    enter_search_term(search_query)
    time.sleep(3)
    click_first_result()


def go_homepage():
    click_position("home")


def full_screen():
    keyboard_controller.press("f")
    keyboard_controller.release("f")


def small_screen():
    keyboard_controller.press(Key.esc)
    keyboard_controller.release(Key.esc)


def play_pause():
    keyboard_controller.press(Key.space)
    keyboard_controller.release(Key.space)


def reload_page():
    keyboard_controller.press(Key.f5)
    keyboard_controller.release(Key.f5)


def go_back():
    keyboard_controller.press(Key.alt)
    keyboard_controller.press(Key.left)
    keyboard_controller.release(Key.alt)
    keyboard_controller.release(Key.left)


def go_forward():
    keyboard_controller.press(Key.alt)
    keyboard_controller.press(Key.right)
    keyboard_controller.release(Key.alt)
    keyboard_controller.release(Key.right)


def mute():
    keyboard_controller.press("m")
    keyboard_controller.release("m")


def find_matched_function(spoken_words):
    keywords = list(no_info_functions.keys()) + list(info_functions.keys())
    for keyword in keywords:
        if keyword in spoken_words:
            return no_info_functions[keyword]


def old_main(spoken_words):
    print(spoken_words)
    if "search" in spoken_words:
        print("searching youtube.....")
        search_youtube(spoken_words)
    elif "full" in spoken_words:
        full_screen()
    elif "home" in spoken_words:
        go_homepage()
    elif "small" in spoken_words:
        small_screen()
    elif "play" in spoken_words or "pause" in spoken_words:
        play_pause()
    elif "first" in spoken_words:
        click_first_result()
    elif "second" in spoken_words:
        click_second_result()
    elif "third" in spoken_words:
        click_third_result()
    elif "back" in spoken_words:
        go_back()
        print("going back........")
    elif "reload" in spoken_words:
        reload_page()
    elif "forward" in spoken_words:
        go_forward()
    hotword.detect_hotword()


# functions that don't require spoken words
no_info_functions = {"full": full_screen,
                     "home": go_homepage,
                     "small": small_screen,
                     "pause": play_pause,
                     "first": click_first_result,
                     "second": click_second_result,
                     "third": click_third_result,
                     "back": go_back,
                     "reload": reload_page,
                     "forward": go_forward}

# functions that do require spoken words
info_functions = {"search": search_youtube}


def main(spoken_words):
    match = find_matched_function(spoken_words)
    if match:
        print(match)
        if match not in no_info_functions:
            match()
        else:
            match(spoken_words)
    hotword.detect_hotword()


if __name__ == "__main__":
    time.sleep(5)
    main(["pause"])