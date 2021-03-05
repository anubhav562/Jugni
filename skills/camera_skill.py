import subprocess


class CameraSkill:

    def __init__(self, action=None):
        self.action = action

    def _generate_text(self):
        return f"The camera has been turned {self.action}"

    def orchestrate_flow(self):

        if self.action == "on":
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif self.action == "off":
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
        else:
            return "Sorry, I could not understand!"

        return self._generate_text()
