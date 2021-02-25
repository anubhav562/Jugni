import speech_recognition
import subprocess
from gtts import gTTS
from playsound import playsound
from configparser import ConfigParser
import requests
import json
import os

from apis.open_weather_api import OpenWeatherAPI


def initiate_jugni():
    recognizer_obj = speech_recognition.Recognizer()

    print("##################################################\n")
    print("########## #      #  #######   ##     #  #########  ")
    print("     #     #      #  #         # #    #      #      ")
    print("     #     #      #  #         #  #   #      #      ")
    print("     #     #      #  #   ####  #   #  #      #      ")
    print("  #  #      #    #   #      #  #    # #      #      ")
    print("   ##        ####    ########  #     ##  #########\n\n")
    print("******* Your very own Virtual Assistant **********  ")
    print("##################################################\n")

    with speech_recognition.Microphone() as source:
        recognizer_obj.adjust_for_ambient_noise(source)
        print("Listening..............")

        while True:
            audio = recognizer_obj.listen(source)
            try:
                text_from_audio = recognizer_obj.recognize_google(audio)
                print(f"Recognised the following: {text_from_audio}")
                if "camera" in text_from_audio:
                    playsound("camera.mp3")
                    subprocess.run('start microsoft.windows.camera:', shell=True)

                elif "weather" in text_from_audio:
                    open_weather_api_obj = OpenWeatherAPI(city="Markham")
                    audio = gTTS(open_weather_api_obj.orchestrate_flow())
                    audio.save("weather.mp3")
                    playsound("weather.mp3")
                    os.remove("weather.mp3")

            except speech_recognition.UnknownValueError as e:
                continue


if __name__ == "__main__":
    initiate_jugni()
