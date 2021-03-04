import os
import speech_recognition
import subprocess
import sys
import threading
import time

from gtts import gTTS
from playsound import playsound
from apis.open_weather_api import OpenWeatherAPI
from nlu_engine.nlu_engine import NLUEngine
from action_dispatcher import intent_to_skill_mapping


######################################################
# Helper functions ###################################
######################################################

def _play_startup_sound():
    """
    This function plays the jugni startup sound in an async fashion.
    It makes the use of threading and opens a daemon in the background.
    :return: None
    """
    threading.Thread(
        target=playsound,
        args=('sounds/jugni_startup_sound.mp3',),
        daemon=True
    ).start()


def _flush_output_to_console():
    jugni_console_text = """
    ##################################################\n
    ######### #      #  #######   ##     #  #########
        #     #      #  #         # #    #      #     
        #     #      #  #         #  #   #      #      
        #     #      #  #   ####  #   #  #      #      
    #   #      #    #   #      #  #    # #      #      
      ##        ####    ########  #     ##  #########\n 
    ******* Your very own Virtual Assistant **********
    ##################################################\n
    """

    for char in jugni_console_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03) if char != " " else None

####################################################
# Initiate Jugni ###################################
####################################################


def initiate_jugni():
    _play_startup_sound()
    _flush_output_to_console()

    time.sleep(0.1)

    recognizer_obj = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        recognizer_obj.adjust_for_ambient_noise(source)
        print("Listening..............")

        while True:
            audio = recognizer_obj.listen(source)
            try:
                text_from_audio = recognizer_obj.recognize_google(audio)
                print(f"Recognised the following: {text_from_audio}")

                nlu_engine_obj = NLUEngine()
                intent, slots = nlu_engine_obj.detect_intents_and_slots(sentence=text_from_audio)
                print(f"Detected the following intent: {intent}, with the following slots: {slots}")

                skill_obj = intent_to_skill_mapping.get(intent)(**slots)

                audio = gTTS(skill_obj.orchestrate_flow())

                audio.save("generated_answer.mp3")
                playsound("generated_answer.mp3")
                os.remove("generated_answer.mp3")

                # if "camera" in text_from_audio:
                #     playsound("sounds/camera.mp3")
                #     subprocess.run('start microsoft.windows.camera:', shell=True)
                #
                # elif "weather" in text_from_audio:
                #     open_weather_api_obj = OpenWeatherAPI(city=slots[0]["city"])
                #     audio = gTTS(open_weather_api_obj.orchestrate_flow())
                #     audio.save("weather.mp3")
                #     playsound("weather.mp3")
                #     os.remove("weather.mp3")

            except speech_recognition.UnknownValueError:
                continue


if __name__ == "__main__":
    initiate_jugni()
