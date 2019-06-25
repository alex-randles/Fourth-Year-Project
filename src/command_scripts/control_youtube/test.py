import sys


def remove_stop_words(spoken_words):
    stop_words = ["for", "search", "youtube", "a"]
    # removed = [word for word in spoken_words if word not in stop_words]
    for word in spoken_words:
        print(word)
        if word in stop_words:
            spoken_words.remove(word)
            stop_words.remove(word)
            print(word)
    new_search_string = " ".join(spoken_words)
    print(new_search_string)
    return new_search_string


print(remove_stop_words(sys.argv[1:]))