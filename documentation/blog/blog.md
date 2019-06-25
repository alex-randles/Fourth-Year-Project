# Voice Assistant Raspberry Pi 

Alex Randles

## My First Blog Entry 27/09/18

This is my first blog entry.

I'm currently at the first stage of thinking of a good project idea, I've a big interest in the internet of things, which are physical devices 
that are controlled by wifi etc. I was possibly thinking of trying to unlock a car with a bluetooth activated key fob but I'm not sure if it
would tie greatly in with my course as it requires more engineering then coding etc. 

The second idea I had was to flash an android phone and install my own custom android rom onto with features I would like to have. I could also 
try get a custom back for the phone made which would make it seem like I've made my own android phone. I'm unsure of this idea as I don't know
if the complexity of changing the operating system to suit my own needs would be good enough. 

I will finalise my project idea in the second week.



## My second Blog Entry 1/10/19

During the second week I discovered something that completely changed the direction of my project. This was the Raspberry Pi which is one of the smallest computer's created. The latest model called the 3 B+ really had some amazing features already built into it. 

I watched numerous youtube videos about projects that were made using this simple but powerful computer. The projects made that were of the most interest to me were a Raspberry Pi mobile phone and a voice assistant raspberry pi.

I felt the raspberry pi mobile phone couldn't have been improved as much as I'd like to. I also felt the physical size of the device wouldn't really cut it for a mobile phone. 

The voice assistant raspberry pi seemed like a more feasible idea as there has been similar devices made but with little functionality. I am going to add more raspberry pi modules to improve functionality. I want more than just voice queries being answered by the device. I will work more on this before I write my proposal.*



![Raspberry Pi 3 Model B+](docs/blog/images/Raspberry-Pi-3-Model-BPlus-side.jpg)

## My third Blog Entry 5/10/19

I have completed my project proposal and uploaded it onto gitlab. I also ordered my raspbery pi to get use to the features of it. 

I now had to look for a supervisor which would be familiar with the raspberry pi to ensure I got the support I needed on my project. 

Talking with fellow students I found that Cathal Gurrin had a good knowledge of the workings of a raspberry pi. I contacted Cathal and arranged a meeting to propose my idea to him.

I met him in the Helix, had a quick conversation then I proposed my idea to him. He was happy to supervise it and guided me in the right direction. He told me told
me to research the matrix creator developement board for the raspberry pi. 



## My fourth Blog Entry 12/10/19

I researched the matrix creator board and found it would be great for adding additional functionality to my project. It includes a number of features such as
NFC, IR blastr/reciever, Microphone array, LEDs etc. I now had to order the part which was more difficult then I thought, I tried many suppliers but most would
not ship to Ireland. I worked around this by getting it shipped to the Northern Irish parcel motel which would then transfer it to my local parcel motel depot.

I met with Cathal for the second time to discuss my project proposal and possible features. 

![Matrix Creator Board](docs/blog/images/MATRIX Creator Dev Board.jpg)

## My fifth Blog Entry 24/10/19

Next was project proposal approval. I wrote my project proposal and then presented it to the examiners. I included a vague idea of what features I would like
my project to have. The panel thought it was an overall idea but were worried the vaguness of what features I would include was not good enough. They also
reminded me that I had to write the functional specification in week 9. They declined my proposal and told me to come up with key features I will definetely 
be including in my project and my spec then from there to add more features on. 

I know had to meet with my supervisor to discuss this in order to get my project approved. 


## My sixth blog Entry 13/11/18

I met with my supervisor and came up with a narrowed down list of functions that I would hop that my final
project would definetely have. I included these key functions in my new proposal and generally tidied up
my proposal.

I thought my proposal was ready for approval. I was wrong, my second proposal was said to include functions that were seen as too ambiguous, they were worried 
I would be unable to implement the functions I had included in the proposal and were worried that when it comes to my demo in the summer I'd present a project that
was a 'a range of unconnected half completed bits and pieces of software.'. This was very dishearting as I was confident in my ability to get all these functions working.
I now became very worried about the prospect of having to change my project idea completely. I understand they are trying to look out for me but this has me quite worried
as I've already started working on the project and functional specification. I will now write a new proposal following the feedback given and hope to finally get approved. 

## My seventh blog entry 15/11/18

Today my proposal was finally approved, took much more work then expected to get approved but im delighted! There was times I was thinking of changing my 
project idea to something that would be easily approved but I would much rather do a project I'm interested in. I've about 30% of the functional specification
done so far.

I've working on the project itself aswell. I got it to turn off my tv at home with a 'turn tv off' voice command but the code I'm using is not optimized and 
was more of brute force approach. I will work on the code more in the next few weeks and try build up a library of scripts to run when a voice command is
heard. 

![happy](docs/blog/images/happy.jpg)

## My eight blog entry 27/11/18

Today I committed my functional spec to the doc directory in my repo. I've been working on the functional specificaiton over the past two weeks trying to ensure I create a high standard one that sets out the functionality of the system
and how it will be achieved. It has helped me to think much deeper about my project idea and how different components will interact with eachother. I carried out a
huge amount of research while writing the functional specification and this will really help me when designing my project. 

I've also been working on setting up the structure for each of my directory's in my system to ensure performance is optimal. 

![fileStructure](docs/blog/images/fileStructure.gif)

## My ninth blog entry 14/12/18

Over the past few weeks I've made decisions about my system structure and how each function will interact with the system. The system design has a hierachial structure with the
speech recognition software at the highest level and each of the function code at a lower level. The system will work by translating the users speech into text and then run
the code relating to that command. Each function will have its own directory that contains all the code it needs to execute.


## My tenth blog entry 31/12/18

I have been carrying out testing with a number of different python speech recognition packages. I wan't to ensure that the speech recogniton I'm using
is fast, accurate and reliable. 
```
The speech recognition services available are:
                                                CMU Sphinx (works offline)
                                                Google Speech Recognition
                                                Google Cloud Speech API
                                                Wit.ai
                                                Microsoft Bing Voice Recognition
                                                Houndify API
                                                IBM Speech to Text
                                                Snowboy Hotword Detection (works offline)
```

I carried out a number of test on each translation service and found that google speech recognition was the most accurate. 


![textToSpeech](https://gitlab.computing.dcu.ie/randlea2/2019-ca400-randlea2/blob/master/docs/blog/images/text-to-speech.png)


## My eleventh blog entry 20/12/18

Over the past few weeks I've been studying for my exams but I have made some progress on my project. I have been deciding on 
which text-to-speech application I will use to speak to the user. 

The following is the result of my research:
```
        1. gTTS (Google Text-to-Speech) - Python package available, i found that while this package sounded semi- real
        it requires the sound to be saved to a file and then playing that file. This package required an internet connection
        and had a slow response time. 
        2. espeak - This was available with a linux application or a python wrapper. This didn't require the audio to be 
        saved to a file but the voice was completely un-human sounding.
        3. Pyttsx - python package available. Unforunately I could only find a python2 compabile version and it also sounded
        un-human sounding.
        4. pico2wave - A linux application which required no internet connection, returned the audio quickly and sounded 
        like a human. This will be the text-to-speech application I will be using for my project. 
        
        Result: pico2wave
```

## My twelfth blog entry 9/01/19

I turned my attention from the user interaction aspect of my project and focused on the scripts for each command. I knew these would follow the same structure regardless of the
speech speaking and speech recognition packages I used. I focused on news commnad ............
        
My twelfth blog post 18/01/19 

I have finished my exam's so I can now start to focus on my project. I want to get to main features I stated in my project proposal implemented. I have been having issues with 
the setting the matrix creator as a default microphone. After a lot of tinkering I edited the alsa mixer settings for the raspberry pi. This took much more time then I expected
which is annoying. The microphone array quality is quite good but I won't know its real accuracy till I try it out with voice commands. 

Next I've installed the python speech recognition package, I will be using the google speech services from this package to translate my text. I have tried it with recorded 
speech files and it translates them correctly so far. The only problem I'm having is with the time it takes to translate the speech and also implementing it so it will 
record speech directly from the microphone and then start translating once the person has stopped speaking. 


```
pcm.!default {
  type asym
   playback.pcm {
     type plug
     slave.pcm "hw:0,0"
   }
   capture.pcm {
     type plug
     slave.pcm "hw:2,0"
   }
}
```



## My thirteenth blog post 25/01/19

Over the past week I have implemented the speech recongition package to record speech while a person is speaking then start translating once they have stopped speaking.
This has sped up the time it takes to translate the users speech but now another problem has presented itself. After repeated translations the raspberry pi crashes!.

I have tried reinstalling the speech recognition packages, changing the code, googling possible causes, checking the system logs, factory resetting the raspberry pi but nothing has fixed it.
This is a real set back as this is the only package I can find which effectively translates speech and can translate directly from the microphone input. 

I have spent days searching for a possible replacement speech recognition software but cannot find one that is as efficent and accurate. I was thinking about trying to use
a hotword detector such as snowboy and then set up each of my commands to be run when a combination of hotwords are said but this will limit my projects functionality to 
only commands that don't require actually speech translation e.g play "name of song". 

I turned my attention from scripting language speech recogntion software to linux speech recognition software. I found multiple results but none were accurate enough or had been
since depreciated.

             ```                                                     
             Linux speech recognition software results:
                                                                    Julius - not open source 
                                                                    CMU sphinx - lacks accuracy 
                                                                    Kaldi - translating speed is not fast enough 
                                                                    Dragon NaturallySpeaking - requires use of virtual machine 
                                                                    Jasper - has since been depreciated
             ```                                                     
## My fourteenth blog entry 01/02/19 

I have written a script to run a specific led configuration on the matrix creator when the device is speaking to the user and when its listening to the user. I have decided
on all white for speaking and all red for listening. Since the matrix creator documentation is so poor, I had to do a lot of my own research on how to communicate to it using 
zero mq which is a high-performance asynchronous messaging library. It uses the the local host and a number of ports to communicate with the device. I've also noticed the 
matrix creator can be quite a confusing device. 

I've noticed one day the code for it will run perfectly, next day without changing any code. I put the matrix creator back on the raspberry pi 
gpio pins and the pi is no longer able to communicate with the matrix creator. This can normally be fixed by removing it and putting it back on but its not always the case.


![leds](docs/blog/images/white_leds.jpg)
![leds](docs/blog/images/red_leds.jpg)

## My fifteenth blog entry 08/02/19 

After setting up the operating system for the matrix creator and learning how to use it, I still had the speech recogntion problem....

I thought maybe the package can only run stable using python2 rather then python3, so I install the package for python2 and python3 on the factory reset system. I have been
backing the system up reguarly using my google drive account. I then ran my code using both versions. At first I thought this fixed my problem but after a number of translations
the system crashed again!. 

I was hopeless and thought my project may have to use a fixed length audio recording to record the persons speech but this would really down grade the overall system. I finally 
thought of a solution.

Use linux software to record the audio but not the standard "arecord" on the command line but software that will detect silence, then records when it detects noise and then 
stops recording once it hears no more speech. I found great software that could do this called sox. It allows you to pass to it paramaters for the level and length of noise and 
silence it must hear before it starts/stops recording. I now needed to find out the optimal configuration to record while the person is speaking the stop straigh away.

```
    Configuration: sox -t alsa default ./record.wav silence 1 0 3% 1 1.0 1%") 
    # first 3 are input when to start recording when sound is 5% and stop recording when sound less then 5% and 1 second gap  
```


I could then transmit this recording to the google speech translation service and recieve back the text to the translated speech! 

## My sixteenth entry 21/02/19 

Met with my supervisor, Cathal Gurrin today to discuss progress so far and whether I would have to acquire ethical approval. 
Since my project would require extensive user testing I would have to seek ethical approval. He informed me as to which forms
I would have to complete. 

After the form is completed I would have to send them to him for inspection then I submit them to my Git repo. 




## My seventeenth entry 26/02/19 


Met with my supervisor, Cathal Gurrin today to discuss all the functionality I had and informed him that I had all the sensors integrated fully (uv, temperature, humidity, gyro etc).
We brainstormed ideas for a smart feature such as turning on a fan when it gets below a certain temperature and turning on a light when it becomes
dark but we didn't fully decide on a feature that I should implement. 

He suggested meeting when back from his work trip in two weeks to decide on the feature......




## My eighteenth first blog entry 1/03/19 

Since my meeting with Cathal, I've been quite focused on getting an automated feature working on my project. We discussed possible turning on a fan/heater when the temperature reaches
a certain level. I spent the next few days implementing all the sensors of the matrix creator. The matrix creator includes many sensors that can retrieve various readings.
These could be used to automate a number of functions. 

```
        Matrix creator sensors:
                                - Ultraviolet light sensor
                                - Humidity sensor 
                                - Pressure sensor
                                - Temperature sensor 
                                - Acceleration sensor
                                - Gyro sensor 
                                - Altitude sensor 
```

I implemented them using python and javascript, this would allow me to have more flexibilty when implementing them into a program. 

## My nineteenth second blog entry 4/03/19

Over the weekend I was thinking about functions I would like automated around my house that would be most useful. When I want to go to sleep at night I would normally ask somebody 
walking by my room to turn off the main lights but then I'd be unable to see anything in my room. (I don't like going to sleep straight away). I would then have to get out of my bed 
and slumber acorss the room to turn the lamp on.

I thought it would be great if I could turn on my lamp automically when the main light in my room is turned off.... 

I had just what I required to implement this! I could use the UV light sensor on my matrix creator to turn on the light when it doesn't detect any light. I experiemented with 
the sensor and found when the UV reading is at 0, it should turn on the light. I could use the zigbee ikea smart outlet I had bought to turn on the light when the matrix creator 
UV reading is 0. The raspberry pi communicates with the matrix sensors through a number of ports using the zero mq messaging protocol. I wrote all the code and tested it. 

It worked but I noticed it would only turn on when the UV reading is 0 but it would stayed turned on when the UV reading is greater then 0. This was an issue. After changing some 
of the code, I had it working perfectly!. 

I added a quick demo video to my google drive to show my supervisor.

Link: https://drive.google.com/file/d/1Br7SFKhRV6vEFsCjSwCBTBGTIdsk3r0X/view?usp=sharing
                        

## My twentieth blog entry 05/03/19 

I have placed a heatsink on the Raspberry Pi in order to overclock the CPU. I couldn't use a fan as it wouldn't fit under my Matrix creator board. I used a testing bash file that would max at the CPU and carry out a number of test. I tested the changing it from 1.4GHz -> 1.45GHz -> 1.5GHz -> 1.55GHz. I didn't go any higher as I've read this is very unstable and may crash the system (especially without a fan) : https://www.babahumor.com/overclock-settings-raspberry-pi-3/ 


Picture of heatsinks 

![heatsink](docs/blog/images/heatsink.JPG)

Testing file 
```
#!/bin/bash
clear 

## show CPU frequency and temperature
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
vcgencmd measure_temp 

## system bench to force CPU to turbo speed 
sysbench --test=cpu --cpu-max-prime=1000 --num-threads=4 >/dev/null 2>&1

## show CPU frequency again 
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq

## longer system bench to measure stability and temperature
sysbench --test=cpu --cpu-max-prime=50000 --num-threads=4 run 

# show CPU frequency and temperature 
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
vcgencmd measure_temp 
```

Results without overclock - 1.4GHz
```
600000
temp=58.5'C
600000
sysbench 0.4.12:  multi-threaded system evaluation benchmark

Running the test with following options:
Number of threads: 4

Doing CPU performance benchmark

Threads started!
Done.

Maximum prime number checked in CPU test: 50000


Test execution summary:
    total time:                          480.9027s
    total number of events:              10000
    total time taken by event execution: 1923.2722
    per-request statistics:
         min:                                115.73ms
         avg:                                192.33ms
         max:                                529.58ms
         approx.  95 percentile:             298.57ms

Threads fairness:
    events (avg/stddev):           2500.0000/10.05
    execution time (avg/stddev):   480.8180/0.06

1400000
temp=78.4'C
```


Result with overclock - 1.55GHz
```
## Results

600000
temp=60.1'C
600000
sysbench 0.4.12:  multi-threaded system evaluation benchmark

Running the test with following options:
Number of threads: 4

Doing CPU performance benchmark

Threads started!
Done.

Maximum prime number checked in CPU test: 50000


Test execution summary:
    total time:                          339.6370s
    total number of events:              10000
    total time taken by event execution: 1358.3624
    per-request statistics:
         min:                                121.04ms
         avg:                                135.84ms
         max:                                218.84ms
         approx.  95 percentile:             136.65ms

Threads fairness:
    events (avg/stddev):           2500.0000/10.56
    execution time (avg/stddev):   339.5906/0.05

155000
temp=77.4'C
```


There is quite a difference in the total execution time (140 seconds)!



## My twenty first blog entry 7/03/19 

During my meeting with Cathal Gurrin we discussed adding additional functionality
to the system and after some brain storming. We decided having the abiltity to send emails
with be of great benefit to the user.... 

I done some research after my meeting with cathal to see if that was possible with python and 
found that python has a built in package called SMTP (Simple mail transfer protocol) which can 
connect to the gmail server and send emails. 

The python documentation on SMTP: https://docs.python.org/2/library/smtplib.html really help when writing
the code. 

Code for sending an email: 


```python
		## connect to gmail smtp server
		gmailServer = smtplib.SMTP("smtp.gmail.com:587") 
		gmailServer.ehlo()
		## start connection 
		gmailServer.starttls() 
		## login to server
		gmailServer.login(emailAddress,password)
		## create the email
		message = "Subject: {}\n\n{}".format(subject,messageContent)
		## send email 
		gmailServer.sendmail(emailAddress,recieverEmailAddress ,message) 
		## close the connection
		gmailServer.quit()	
```

The system prompts the user for recievers email, the subject of the email and the content
of the body, then send its using the SMTP protocol. 


## My twenty second 10/03/19

I have been focusing on improving the speech recognition aspect of my system as I feel it was
lacking accuracy and reliability. I decided to research sound recorder python packages and came 
across one I have previously seen called pyaudio. 

I wanted to write a script that could record audio while sound is detected and stop recording once
the sound is below a certain threshold. I could then send this audio to a speech-to-text translation
service and receive the translated text back. 

I hoped using just python for this one speed up the result time and improve the accuracy. I did lots of 
research and found lots of information on pyaudio, the following site was quite useful: https://people.csail.mit.edu/hubert/pyaudio/docs/

After numerous iterations I finally came up with a quite efficent speech recorder, it took a lot of testing but heres the code..

```python
def recordAudio(): 
	## start pyaudio 
	audio=pyaudio.PyAudio()
	audioStream =audio.open(format=pyaudio.paInt16,channels=2, rate=44100, input=True,frames_per_buffer=1024)
	return audio, audioStream 


def detectAudio(audioStream):
	## maximum length of silence 
	maxSilence = 43
	silentCounter = 0 
	## has a word been deteced 
	wordsSpoken = False 
	dataContainer =[]
	## while silence is not greater than 1 second 
	while silentCounter < maxSilence: 
		## start taking in data
		data= audioStream.read(1024)
		dataChunk=array.array('h',data)
		soundLevel =max(dataChunk)
		## threshold for silence 
		if soundLevel > 1000:
			wordsSpoken = True 
			dataContainer.append(data)
		elif wordsSpoken == True:
			silentCounter+=1
	return audioStream, dataContainer

def writeAudio(fileName, audioStream, audio, dataContainer):
	## get non silent recording 
	#audioStream = detectAudio() 
	# stop recording 
	audioStream.stop_stream()
	audioStream.close()
	## get pyaudio 
	#audio = recordAudio() 
	audio.terminate()
	#writing to file
	audioFile=wave.open(fileName,'wb')
	## set paramaters 
	audioFile.setnchannels(2)
	audioFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	audioFile.setframerate(44100)
	## add frames to the file  
	audioFile.writeframes(b''.join(dataContainer))
	audioFile.close()	
```

## My twenty third blog entry 14/03/19 

I was kindly given a Raspberry Pi camera from my supervisor. I set up it and found it suprisngly easy to do so. First I had to put 
the camera ribbon cable into the Raspberry Pi connector and then change the configuration to enable the camera. I then looked into 
how to take pictures and record videos, the Raspberry Pi documentation was very useful: https://www.raspberrypi.org/documentation/usage/camera/raspicam/README.md

```
Take a picture: raspistill -o cam.jpg
Record 10 second video: raspivid -o video.h264 -t 10000
```

![camera](docs/blog/images/pi_camera.jpg)
![picture](docs/blog/images/camera_picture.jpg)
 
I had to integrate with python, I found there was a great module called "picamera", the documentation was very useful for setting it up: https://picamera.readthedocs.io/en/release-1.13/

```python
Taking a picture with python:
	from picamera import PiCamera

	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	# Camera warm-up time
	sleep(2)
	camera.capture('foo.jpg')

```

Next I had to think of something useful to do with it, I'm hoping to make video calls using it.....

## My twenty fourth blog entry 25/03/19

After numerous attempts I've finally got the hotword for the system implemented using snowboy hotword detector. 
I have yet to decide on the hotword that will be used to wake up the system so for now I'm using "snowboy".....

The reason for it wasn't working before I had a mistake within the audio input configuration file making it unable to
detect sound from the matrix creators microphone. 

The code for training a hotword with snowboy is quite simple. 
	1. Get an API key from the snowboy website 
	2. Record the hotword 3 times using the following commands 
	arecord hotword1.wav -f S16_LE -r 16000 -d 5
	arecord hotword2.wav -f S16_LE -r 16000 -d 5
	arecord hotword3.wav -f S16_LE -r 16000 -d 5
	3. Send it to the snowboy server
	python training_service.py 1.wav 2.wav 3.wav hotword.pmdl
	4. The result with be saved as a hotword.pmdl, pdml stands for personal model which means
	it will only work with my voice but this personal model can be uploaded to the snowboy website
	where others will record the hotword and this will train a neural network to create a .umdl
	file which is universal and will work with anyone. 

To implement a function call when the hotword is detected: 
	
	import snowboydecoder

	def hotwordDetected():
		## hotword called when hotword detected 
		## function code goes here

	detector = snowboydecoder.HotwordDetector("hotword.pmdl", sensitivity=0.5, audio_gain=1)
	detector.start(hotwordDetected)
	
This works quite accurately,  the only problem is when I try to record what the user is saying straight after
this using my speechRecorder function that records the users speech using pyaudio an overflow buffer error is
created!

## My twenty fifth blog entry 28/03/19

It was brought to attention that security could be an issue with my project.... 

Since you'll be able to control smart home devices, send & read emails allowing anyone to use the device 
could become an issue. I've decided to add another feature that allows the user to set whether the device
uses a personal hotword or an universal hotword. 

It will initially be set to use an universal hotword so anyone can wake up the device but this can be changed 
using the security command. 

I will store which level of security is currently set in a database. 

For a universal hotword which anyone can use:
```python
	detector = snowboydecoder.HotwordDetector("snowboy.umdl", sensitivity=0.5, audio_gain=1)

```


For a personal hotword that only one person can use:
```python
	detector = snowboydecoder.HotwordDetector("snowboy.pmdl", sensitivity=0.5, audio_gain=1)

```

The security database will look like this if security lock is off:
```python
	[(u'false', u'snowboy.umdl')]

```
And if the security lock is on:
```python
	[(u'true', u'snowboy.pmdl')]

```

This will be checked each time a person tries to use the hotword and depending upon the settings they may or 
may not be allowed. 

## My twenty sixth blog entry 11/04/18 


Met with my supervisor, Cathal Gurrin to discuss all the functionality i've fully integrated and he was quite happy with it.
We discussed the upcoming project demonstration and expo to as what I should expect from them. He gave me great tips for 
each of them. 

I was only told I should have three pieces of code which I can show to the examiners and these could be within seperate 
scripts. 

I told him about all the testing I've done so far and he suggested drafting in more users for the user testing which I was 
happy to do. 




## My twenty seventieth entry 12/04/18 

I have implemented the  read email command which will read any unread emails and marked them as read afterwards.
I've been having trouble with exception handling if there are no unread emails but should be able to figure this 
out with some more thinking. Instead of using smtplib such as I did for my script to send emails, I used a different 
python package called imap which can search through the gmail inbox's. 

Code snippet to retrieve all the unread emails. 

```python
		gmailUrl  = "imap.gmail.com"
		connection = imaplib.IMAP4_SSL(gmailUrl) 
		connection.login(configuration.emailAddress, configuration.password) 
		connection.select("INBOX") 
		## retrieve all the unread email id's
		(returnCode, emails) = connection.search(None, '(UNSEEN)')
		unreadEmailNumbers = emails[0].split()
		## retrieve the latest unread email 
		latestUnreadNumber  = unreadEmailNumbers[-1]
```
I will have to make some decisions about how it speaks the output but this script works a charm!. I've also been doing lots
of work on integrating all the different components of the system and also testing. 

I'd also like to add a few more features but I will first get all the features currently integrated correctly and work on 
effiency . 


## My twenty eight entry 20/04/19

I found that the command script which was activated by the user e.g news, weather was taking alot longer then expected. After doing 
research I found out the command as a seperate python script would increase execution speed. I decided to package my command's into 
a "command_scripts" package. To make the package visible to python I had to add the path to the python path, I decided to add it
at the front so it would be checked by the interpreter first. 

Within this package with be a hierachy of modules which would each carry out there own function. 


For example if I wanted to import the news module

```python
            # import the command's package
            import command_scripts
            # import the news module
            from command_scripts import news 
```

This greatly speed up execution of commands! I have all the commands nearly integrated, I just need to ensure that if a command fails to 
execute that I will return to the normal state. Lots of testing makes these fault points more prominent. 

### Testing

I've also been doing a lot of testing using pythons unittest and also carrying out user testing which has really helped me discover flaws
which I wouldn't have noticed testing it by myself. 


## My twenty ninth blog entry & final blog post 05/05/19 

Over the past while I have been focused more on exams but I am also adding the final touches to my project. These
include fix any errors that I have discovered while testing. I have been carrying out extensive unit testing,
component testing and user testing. 
 
One of the errors I noticed was with the IR sensor and the sound output on the Raspberry Pi. I had to buy an external
USB sound card to connect the speaker through as the auxiliary input was being disrupted by the serial transition of the matrix creator. 

I have also been discussing with Cathal about my demonstration. He has given me good pointers about how I should present and told
me to practice it repeatedly to ensure I give my best demonstration possible. 

While the final project is not perfect by any means, I am happy with the final implementation and have enjoyed
the learning experience involved with developing it. 



