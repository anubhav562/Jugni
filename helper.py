import os
import sys
import threading
import time

from gtts import gTTS
from playsound import playsound


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


def _introduce_jugni():
    playsound("sounds/jugni_introduction.mp3")
    time.sleep(0.5)
    playsound("sounds/jugni_introduction_2.mp3")


def _read_text(text):
    audio = gTTS(text)
    audio.save("generated_response.mp3")
    playsound("generated_response.mp3")
    os.remove("generated_response.mp3")


def _play_response_to_user(response_from_skill):

    if type(response_from_skill) == str:
        _read_text(response_from_skill)

    elif type(response_from_skill) == dict:

        for response in response_from_skill["list_of_utterances"]:

            _read_text(response)

            if response_from_skill["interval_sound_required"]:
                playsound("sounds/interval_sound.mp3")
            else:
                time.sleep(0.4)
