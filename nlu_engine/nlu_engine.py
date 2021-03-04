import os
from snips_nlu import SnipsNLUEngine


class NLUEngine:

    def __init__(self):
        self.nlu_engine_object = SnipsNLUEngine.from_path(
            os.path.join(os.getcwd(), "nlu_engine", "persisted_engine")
        )

    def detect_intents_and_slots(self, sentence):
        parsed_output = self.nlu_engine_object.parse(sentence)
        intent_name = parsed_output.get("intent", {}).get("intentName")
        slots = parsed_output.get("slots", [])

        if len(slots):
            slots = {slot["slotName"]: slot["value"]["value"] for slot in slots}

        return intent_name, slots
