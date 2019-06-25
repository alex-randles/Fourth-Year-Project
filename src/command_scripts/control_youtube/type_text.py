from pynput.keyboard import Controller as KeyboardController
import time

keyboard = Controller()


def type_sentence(sentence):
    for char in sentence:
        keyboard.press(char)
        keyboard.release(char)


if __name__ == "__main__":
   type_sentence("Hello")
