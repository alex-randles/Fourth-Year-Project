# test if system finds correct command module for the string given
import unittest
import sys
import json
from log_results import record
# unit being tested
from command_recogniser import find_module_location
# we first need to find the command
from command_recogniser import find_command


# to run: python -m unittest test_module_locator
# example sentences
sentence_file = open("./sentences.json", "r")
sentences_json = json.load(sentence_file)


class TestModuleLocator(unittest.TestCase):
    # test_1 will check if the find_command function finds the
    # correct command for a sentence

    # test news command
    def test_1(self):
        #               (search,    example user sentence,     expected result)
        for sentence in sentences_json["news"]["sentences"]:
            # find command first then location
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "news.get_news")
    # test send email command
    def test_2(self):
        for sentence in sentences_json["send_email"]["sentences"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "emails.send_email")
    # test translation command
    def test_3(self):
        for sentence in sentences_json["translation"]["translation"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "translation.translate_language")
    # test information searcher command
    def test_4(self):
        for sentence in sentences_json["search"]["search"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "search_information.search_wiki")

    # test music player command
    def test_5(self):
        for sentence in sentences_json["music"]["sentences"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "music.play_music")

    # test read email command
    def test_6(self):
        for sentence in sentences_json["read_email"]["sentences"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "emails.read_unread_email")

    # test weather command
    def test_7(self):
        for sentence in sentences_json["weather"]["weather"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "weather.get_weather")

    # test tv on command
    def test_8(self):
        for sentence in sentences_json["tv_on"]["sentences"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "tv.turn_tv_on")


    # test tv off command
    def test_9(self):
        for sentence in sentences_json["tv_off"]["sentences"]:
            command = find_command(sentence)
            self.assertEqual(find_module_location(command), "tv.turn_tv_off")


('  \n'
 '  # test turn on the plug command\n'
 '    def test_10(self):\n'
 '        for sentence in example_plug_on_sentence:\n'
 '            command = find_command(sentence)\n'
 '            self.assertEqual(find_module_location(command), "")\n'
 '\n'
 '    # test turn on the plug command\n'
 '    def test_11(self):\n'
 '        for sentence in example_plug_on_sentence:\n'
 '            command = find_command(sentence)\n'
 '            self.assertEqual(find_module_location(command), "music.play_music")\n'
 '            ')



if __name__ == "__main__":
    # execute all test
    unittest.main() 


