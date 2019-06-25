import pyaudio
import wave
import array
import speech_recognition
import signal
import subprocess


#################################
###   speech recognition ########
#################################


def record_audio():
    audio = pyaudio.PyAudio()
    audio_stream = audio.open(format=pyaudio.paInt16, channels=2, rate=8000, input=True, frames_per_buffer=1024)
    return audio, audio_stream


def start_recording(audio_stream):
    # minimum length of recording
    min_time = 30
    time_counter = 0
    # level it must reach to start recording
    volume_threshold = 10
    data_container = []
    while time_counter < min_time:
        ## start taking in data
        data = audio_stream.read(1024, exception_on_overflow=False)
        data_chunk = array.array('h', data)
        sound_level = max(data_chunk)
        # threshold for sound
        print(sound_level)
        if sound_level > volume_threshold:
            data_container.append(data)
        time_counter += 1
    return audio_stream, data_container


def write_audio(file_name, audio_stream, audio, data_container):
    # stop recording
    terminate(audio_stream)
    audio.terminate()
    # writing to file
    audio_file = wave.open(file_name, 'wb')
    audio_file.setnchannels(2)
    audio_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(8000)
    # add frames to the file
    audio_file.writeframes(b''.join(data_container))
    terminate(audio_stream)


def terminate(audio_stream):
    audio_stream.stop_stream()
    audio_stream.close()


def start_translator():
    # stop any other recording 
    audio_file = "speech.wav"
    audio, audio_stream = record_audio()
    # get the audio
    new_audio_stream, data_container = start_recording(audio_stream)
    #  wite the audio to a file
    write_audio(audio_file, new_audio_stream, audio, data_container)
    # translate the audio file to  text
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio_file) as source:
        try:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print(text.lower())
            return text.lower()
        except:
            return ""



if __name__ == "__main__":
    start_translator()

