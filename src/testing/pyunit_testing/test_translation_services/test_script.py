## script to test the speech translation services 
import speech_recognition
import time

def runTest(audioPath):
	# initialize recognizer class 
	recognizer = speech_recognition.Recognizer()
	## translation services we're testing
	services = {"Wit.ai":recognize_wit, "CMU sphinx": recognizer.recognize_sphinx, "Bing": recognize_bing, "Google":recognizer.recognize_google }
	with speech_recognition.AudioFile(audioPath) as source:
		## test using all available services 
		for service in services:
			## read in audio 
			audio = recognizer.record(source) 
			## start timer 
			start = time.time()
			## translate using service from services dictionary 
			result = services[service](audio)
			finish = time.time() 
			## total time taken 
			timeTaken = (finish - start)
			accuracy = calculateAccuracy(result)
			recordResults(service, timeTaken, accuracy, audioPath)
			
def calculateAccuracy(result):
	## string that was actually said
	compare = "this is user testing for the voice assistant"
	## convert to lower case for comparsion 
	result = result.lower() 
	## accuracy of how many words were correctly translated 
	accuracy = len([char for char in result.split() if char in compare.split()]) / len(compare.split())
	return accuracy 
	
	
	
def recordResults(name, time, accuracy, audioFile):
	## get only the audio files name not full path
	audioFile = audioFile.split("/")[-1] 
	# record time taken to translate file 
	with open("time_results.txt","a") as timeResults:
		timeResults.write("{} took {} seconds to translate audio file: {}\n".format(name, time,audioFile))
	
	# record the accuracy of the file
	with open("accuracyResults.txt", "a") as accuracyResults:
		accuracyResults.write("{} accuracy was {} with audio file: {}\n".format(name, accuracy, audioFile))
	

def main(audioPath):
	## carry out test with all users audio file 
	for path in audioPath:
		runTest(path)
		
		
if __name__ == "__main__":
	## users audio files saying predifined phrase
	audioFiles = ["/home/pi/2019-ca400-randlea2/src/testing/unit_testing/test_translation_services/user_4.wav"]
	main(audioFiles) 
