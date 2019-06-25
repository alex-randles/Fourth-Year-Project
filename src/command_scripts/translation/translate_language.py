# version includes led configuration
from py_translator import Translator
import sys
import json
import subprocess

# custom modules
import hotword
import translate_speech
import speak

# json file with all languages
languages_file = '/home/pi/2019-ca400-randlea2/src/command_scripts/translation/languages.json'

# query user for destination language and what they'd like to translate
def query_user(spoken_words):
    if spoken_words is None:
        spoken_words = sys.argv[1:]
    language = search_languages(spoken_words)
    sentence = find_sentence(spoken_words)
    print(sentence, language)
    print(spoken_words)
    if language is None:
        speak.speak_to_user("language not found")
        hotword.detect_hotword()
    return language, sentence


# find the sentence they wish to translate
def find_sentence(sentence):
    # words that wouldn't be apart of the sentence
    new_sentence = [word for word in sentence[1:-2]]
    new_sentence = " ".join(new_sentence)
    print(new_sentence)
    return new_sentence



# find the language from the string
def search_languages(spoken_words):
    # check the languages.json file for matching language
    with open(languages_file) as json_file:
        languages = json.load(json_file)
        for word in spoken_words:
            formatted_word = word[0].upper() + word[1:].lower()
            for language_code in languages:
                if  languages[language_code]["name"] == formatted_word:
                    return formatted_word

    return None



# uses python language translation package
def translate(destination_language, sentence):
    translation = Translator().translate(text=sentence, dest=destination_language).text
    formatted_translation = translation.replace("'", "")
    return formatted_translation




def main(spoken_words):
    # parse the destination language and sentence from user input
    destination_language, sentence = query_user(spoken_words)
    print(destination_language)
    # translate sentence and speak to user
    translation = translate(destination_language, sentence)
    speak.speak_to_user(translation)
    # start hotword again
    hotword.detect_hotword()


if __name__ == "__main__":
    main(sys.argv[1:])
