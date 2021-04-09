class ActionsGuide:

    def __init__(self):
        self.actions_guide_response = {
            "list_of_utterances": [
                "I can currently assist you with the following",
                "Opening an application.",
                "Navigating you to a destination.",
                "Conveying you the weather conditions",
                "and telling you jokes.",
                "Now that you know my super-powers. Please let me know how can I help!"
            ],
            "interval_sound_required": False
        }

    def orchestrate_flow(self):
        return self.actions_guide_response
