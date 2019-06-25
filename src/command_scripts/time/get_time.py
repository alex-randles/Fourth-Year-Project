import os
import time
import subprocess

# custom modules
import speak
import hotword


def get_time():
	# format time in hours, minutes, seconds
	current_time = time.strftime("%I : %M %p")
	return current_time
	

def main():
	current_time = get_time()
	speak.speak_to_user(current_time)
	hotword.detect_hotword()


if __name__ == "__main__":
	main()