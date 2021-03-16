import json
import requests
from configparser import ConfigParser


class JokeSkill:

    def __init__(self):
        self.random_joke_api_endpoint = "https://dad-jokes.p.rapidapi.com/random/joke"
        self.request_header = {"x-rapidapi-key": self._fetch_api_key_from_credentials()}

    @staticmethod
    def _fetch_api_key_from_credentials():
        config_parser = ConfigParser()
        config_parser.read("credentials.cfg")
        return config_parser.get("JokeAPI", "api_key")

    def orchestrate_flow(self):
        response = json.loads(
            requests.get(url=self.random_joke_api_endpoint, headers=self.request_header).content
        )

        buildup = response.get("body", [{}])[0].get("setup")
        punchline = response.get("body", [{}])[0].get("punchline")

        return {"interval_sound_required": False, "list_of_utterances": [buildup, punchline]}


