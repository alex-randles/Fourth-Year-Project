# check if security changer passes test
from hotword import change_security, get_hotword_set
import json
import unittest

sentence_file = open("/home/pi/2019-ca400-randlea2/src/testing/unit_testing/sentences.json", "r")
sentences_json = json.load(sentence_file)


class TestSecurityCommand(unittest.TestCase):
    def test_1(self):
        # change security and check if correct hotword is set
        change_security("turn security on")
        self.assertEqual(get_hotword_set(), "/home/pi/2019-ca400-randlea2/src/snowboy.pmdl")

    def test_2(self):
        change_security("security on")
        self.assertEqual(get_hotword_set(), "/home/pi/2019-ca400-randlea2/src/snowboy.pmdl")


    def test_3(self):
        change_security("turn security off")
        self.assertEqual(get_hotword_set(), "/home/pi/2019-ca400-randlea2/src/snowboy.umdl")


    def test_4(self):
        change_security("security off")
        self.assertEqual(get_hotword_set(), "/home/pi/2019-ca400-randlea2/src/snowboy.umdl")


    sentence_file.close()


if __name__ == "__main__":
    # execute all test
    unittest.main()

