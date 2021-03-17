import random
import sys

from playsound import playsound
from helper import _read_text


POSSIBLE_RESPONSES = [
    "Bye! Hope that I will talk to you soon. Terminating Now.",
    "Bye! Will see you soon. Take care. Shutting down now.",
    "See you later! Bye and hope you have a great day ahead! Terminating Now.",
    "See you later! Jugni signing off!",
    "How lucky I am to have someone which makes it difficult for me to say goodbye. Bye, I will miss you!",
    "Going for a quick nap, will see you soon."
    "Going for a sleep. Bye!"
]


class TerminateJugni:
    def __init__(self):
        self.termination_sound_path = "sounds/jugni_terminate.mp3"

    def orchestrate_flow(self):
        response = POSSIBLE_RESPONSES[random.randint(0, len(POSSIBLE_RESPONSES)-1)]
        _read_text(response)
        playsound(self.termination_sound_path)
        sys.exit(0)
