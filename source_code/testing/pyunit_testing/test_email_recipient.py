# test given a string the send_email script will find correct recipient
import unittest
import sys
import json
from log_results import record
# unit being tested
from command_scripts.emails.send_email import find_recipient

# to run: python -m unittest test_email_recipient
# example sentences
sentence_file = open("./sentences.json", "r")
sentences_json = json.load(sentence_file)
email_sentences = sentences_json["send_email"]["sentences"]


class TestEmailRecipient(unittest.TestCase):
    # test_1 will check if the find_command function finds the
    # correct command for a sentence
    # test news command
    def test_1(self):
        self.assertEqual(find_recipient(["send", "an", "email", "to", "alex"]), "alexrandles0@gmail.com")

    def test_2(self):
        self.assertEqual(find_recipient(["send", "an", "email", "to", "sophie"]), "sophieanne.randles2@mail.dcu.ie")


    def test_3(self):
        self.assertEqual(find_recipient(["send", "an", "email", "to", "nicky"]), "nickyrandles@gmail.com")

    def test_4(self):
        self.assertEqual(find_recipient(["send", "an", "email", "to", "nicholas"]), "nicholasrandles@hotmail.com")

    sentence_file.close()


if __name__ == "__main__":
    # execute all test
    unittest.main() 

