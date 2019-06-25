# test given a string the send_email script will find correct recipient
import unittest
import sys
import json
from log_results import record
# unit being tested
from command_scripts.translation.translate_language import search_languages

# to run: python -m unittest test_language_finder
# example sentences
sentence_file = open("./sentences.json", "r")
sentences_json = json.load(sentence_file)


class TestLanguageFinder(unittest.TestCase):
    # test_1 will check if the find_command function finds the
    # correct command for a sentence
    # test news command
    def test_1(self):
        self.assertEqual(search_languages(["translate","how", "are", "you", "to", "english"]), "English")

    def test_2(self):
        self.assertEqual(search_languages(["translate","how", "are", "you", "to", "french"]), "French")


    def test_3(self):
        self.assertEqual(search_languages(["translate","how", "are", "you", "to", "spanish"]), "Spanish")

    def test_4(self):
        self.assertEqual(search_languages(["translate","how", "are", "you", "to", "german"]), "German")

    sentence_file.close()


if __name__ == "__main__":
    # execute all test
    unittest.main()

