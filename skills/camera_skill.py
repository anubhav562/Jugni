import subprocess
import random

CAMERA_ON_RESPONSES = [
    "The camera has been turned on.",
    "The camera has been activated.",
    "The camera is now turned on.",
    "The camera is activated.",
    "Okay! Camera started.",
    "Camera started."
]

CAMERA_OFF_RESPONSES = [
    "The camera has been turned off.",
    "The camera is now turned off.",
    "Okay! Camera closed.",
    "Camera closed.",
    "The camera has been closed.",
]


class CameraSkill:

    def __init__(self, action=None):
        self.action = action

    def _generate_text(self):
        if self.action == "on":
            response = CAMERA_ON_RESPONSES[random.randint(0, len(CAMERA_ON_RESPONSES)-1)]
        elif self.action == "off":
            response = CAMERA_OFF_RESPONSES[random.randint(0, len(CAMERA_OFF_RESPONSES) - 1)]
        return response

    def orchestrate_flow(self):

        if self.action == "on":
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif self.action == "off":
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
        else:
            return "Sorry, I could not understand!"

        return self._generate_text()
