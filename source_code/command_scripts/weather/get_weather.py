import pyowm
import subprocess

# custom module
import speak
import hotword

API_key = "2ff64af7400b09af0474e377a01a64f2"


def get_forecast():
    weather_connection = pyowm.OWM(API_key)
    observation = weather_connection.weather_at_place("Dublin,ireland")
    weather = observation.get_weather()
    weather_status = weather.get_detailed_status()
    temperature = weather.get_temperature('celsius')
    min_temp = temperature["temp_min"]
    max_temp = temperature["temp_max"]
    weather_forecast = "{} with highs of {} degrees and lows of {} degrees".format(weather_status, max_temp, min_temp)
    return weather_forecast


def main():
    weather_forecast = get_forecast()
    speak.speak_to_user(weather_forecast)
    hotword.detect_hotword()

if __name__ =="__main__":
    main()


