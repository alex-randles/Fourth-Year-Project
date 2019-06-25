# test if system finds correct command for a string of words
import unittest
import sys
import json
from log_results import record
# unit being tested
from command_recogniser import find_matched_keywords


# to run: python -m unittest test_command_finder
# example sentences
sentence_file = open("./sentences.json", "r")
sentences_json = json.load(sentence_file)


class TestCommandFinder(unittest.TestCase):
    # test_1 will check if the find_command function finds the 
    # correct command for a sentence 
    # test news command 
    def test_1(self):
        #               (search,    example user sentence,     expected result)
        for sentence in sentences_json["news"]["sentences"]:
            print(sentence)
            self.assertEqual(find_matched_keywords(sentence)[0], "news")
    # test send email command
    def test_2(self):
        for sentence in sentences_json["send_email"]["sentences"]:
                self.assertEqual(find_matched_keywords(sentence)[0], "send_email")
    # test translation command 
    def test_3(self):
        for sentence in sentences_json["translation"]["sentences"]:
                self.assertEqual(find_matched_keywords(sentence)[0], "translator")
    # test information searcher command 
    def test_4(self):
        for sentence in sentences_json["search"]["sentences"]:
                self.assertEqual(find_matched_keywords(sentence)[0], "search")
                
    # test music player command 
    def test_5(self):
        for sentence in sentences_json["music"]["sentences"]:
                self.assertEqual(find_matched_keywords(sentence)[0], "music")


if __name__ == "__main__":
    unittest.main()  # run all tests
