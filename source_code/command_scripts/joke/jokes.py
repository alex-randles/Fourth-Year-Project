# Command Script for Reading out Jokes
import random
import subprocess
import json

# custom module
import speak
import hotword

def tell_joke(joke_file):
	load_file = open(joke_file)
	joke_list = json.load(load_file)
	random_joke = random.choice(joke_list["jokes"])
	speak.speak_to_user(random_joke)
	hotword.detect_hotword()
	


def main():
	tell_joke("/home/pi/2019-ca400-randlea2/src/command_scripts/joke/jokes.json")


if __name__ == "__main__":
	main()

