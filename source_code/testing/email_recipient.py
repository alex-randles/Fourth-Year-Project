# test given a string the send_email script will find correct recipient
# test if system finds correct command for a string of words
import unittest
import sys
import json
from log_results import record
# unit being tested
from command_scripts.send_email import find_recipient

# to run: python -m unittest test_command_finder
# example sentences
sentence_file = open("/home/pi/2019-ca400-randlea2/src/testing/unit_testing/sentences.json", "r")
sentences_json = json.load(sentence_file)
email_sentences = sentences_json["send_email"]["sentences"]


class TestEmailRecipient(unittest.TestCase):
    # test_1 will check if the find_command function finds the
    # correct command for a sentence
    # test news command
    def test_1(self):
        self.assertEqual(find_recipient(email_sentences[0]), "alex")





