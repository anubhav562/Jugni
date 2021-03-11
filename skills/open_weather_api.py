import json
import random
import requests

from configparser import ConfigParser


TEMPLATED_RESPONSES = [
    "It looks like {city} has {weather_desc} today. Temperature is {temperature} degrees celsius",
    "Currently in {city}, the temperature is {temperature} degrees celsius. It has {weather_desc} today.",
    "Today in {city}, we have {weather_desc}. The temperature is {temperature} degrees celsius.",
    "Today's weather outlook in {city} tends to be {weather_desc}. It's {temperature} degrees celsius outside.",
    "Today tends to be {weather_desc} in {city}. The temperature is currently {temperature} degrees celsius",
    "The temperature is currently {temperature} degrees celsius in {city}. Today there's {weather_desc}.",
    "The forecast for today in {city} is {weather_desc}. The temperature is {temperature} degrees.",
    "The weather in {city} is forecast to be {weather_desc} today."
    "The temperature outside is {temperature} degrees."
]


class OpenWeatherAPI:

    def __init__(self, city=None):
        if city is None:
            city = self._fetch_current_city_from_ip()

        self.city = city
        self.app_id = OpenWeatherAPI._fetch_app_id_from_credentials()
        self.api_endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.app_id}"
        self.api_response = None

    @staticmethod
    def _fetch_current_city_from_ip():
        config_parser = ConfigParser()
        config_parser.read("credentials.cfg")
        api_key = config_parser.get("IPData", "api_key")
        response = requests.get(f"https://api.ipdata.co/?api-key={api_key}").content
        return json.loads(response)["city"]

    @staticmethod
    def _fetch_app_id_from_credentials():
        config_parser = ConfigParser()
        config_parser.read("credentials.cfg")
        return config_parser.get("OpenWeatherAPI", "app_id")

    def _hit_api(self):
        try:
            response = requests.get(url=self.api_endpoint)
            if response.status_code != 200:
                return
            self.api_response = response.content

        except Exception as e:
            print(f"Following exception occurred: {e}")
            return

    def _parse_temperature_from_response(self):
        try:
            temp_in_kelvin = json.loads(self.api_response).get("main", {}).get("temp", None)
            temp_in_celsius = round(temp_in_kelvin - 273.15)
        except Exception as e:
            print(f"Following exception occurred: {e}")
            temp_in_celsius = None
        return temp_in_celsius

    def _parse_weather_from_response(self):
        try:
            weather_desc = json.loads(self.api_response).get("weather", [{}])[0].get("description", None)
        except Exception as e:
            print(f"Following exception occurred: {e}")
            weather_desc = None
        return weather_desc

    def _prepare_text_for_speech_engine(self, temperature, weather_desc):
        selected_response = TEMPLATED_RESPONSES[random.randint(0, len(TEMPLATED_RESPONSES)-1)]
        formatted_response = selected_response.format(
            city=self.city, weather_desc=weather_desc, temperature=temperature
        )
        return formatted_response

    def orchestrate_flow(self):
        self._hit_api()
        temperature = self._parse_temperature_from_response()
        weather_desc = self._parse_weather_from_response()
        text = self._prepare_text_for_speech_engine(temperature, weather_desc)
        return text
