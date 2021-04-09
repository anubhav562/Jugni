import speech_recognition
import time

from action_dispatcher import intent_to_skill_mapping
from helper import _flush_output_to_console, _introduce_jugni, _play_response_to_user, _play_startup_sound
from nlu_engine.nlu_engine import NLUEngine
from playsound import playsound
from skills.web_browser import WebBrowser


####################################################
# Initiate Jugni ###################################
####################################################


def initiate_jugni():
    _play_startup_sound()
    _flush_output_to_console()

    recognizer_obj = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        recognizer_obj.adjust_for_ambient_noise(source)
        _introduce_jugni()
        print("Listening..............")

        while True:
            audio = recognizer_obj.listen(source)
            try:
                text_from_audio = recognizer_obj.recognize_google(audio)

                if text_from_audio.lower() == "terminate":
                    playsound("sounds/jugni_terminate.mp3")
                    break

                print(f"Recognised the following: {text_from_audio}")

                nlu_engine_obj = NLUEngine()
                intent, slots = nlu_engine_obj.detect_intents_and_slots(sentence=text_from_audio)
                print(f"Detected the following intent: {intent}, with the following slots: {slots}")

                if intent:
                    skill_obj = intent_to_skill_mapping.get(intent)(**slots)
                else:
                    skill_obj = WebBrowser(text_to_search_for=text_from_audio)

                response_from_skill = skill_obj.orchestrate_flow()
                _play_response_to_user(response_from_skill) if response_from_skill else None

            except speech_recognition.UnknownValueError:
                continue


if __name__ == "__main__":
    initiate_jugni()
