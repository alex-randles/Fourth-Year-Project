# retrieves information from wikipedia about the user's request
import subprocess
import sys
import wikipediaapi
import time

#custom modules
import speak
import hotword

def format_search_string(spoken_words):
    # extract search string from translated speech
    stop_words = ["what", "is", "a", "the", "who", "an","who", "was"]
    # remove stop words
    search_string = [word.capitalize() for word in spoken_words if word not in stop_words]
    # join with underscore for wikipedia search term
    search_string = "_".join(search_string)
    # remove 's from end of search string if present
    if search_string[-2:] == "'s":
        search_string = search_string[:-2]
    return search_string


def get_information(search_string):
    wiki = wikipediaapi.Wikipedia('en')
    wiki_page = wiki.page(search_string)
    summary = wiki_page.summary
    current_summary = ""
    # get shorter summary
    for summary in summary.split("."):
        current_summary += summary
        # but not too short
        if len(current_summary) > 100:
            format_summary = ''.join(char for char in current_summary if char.isalnum() or char == " ")
            return format_summary
    return summary


def speak_results(results):
    if results != "":
        speak.speak_to_user(results)
    else:
        speak.speak_to_user("No information found")


def main(spoken_words):
    print(spoken_words)
    search_string = format_search_string(spoken_words)
    # print(search_string)
    results = get_information(search_string)
    speak_results(results)
    hotword.detect_hotword()


if __name__ == "__main__":
    main(sys.argv[1])