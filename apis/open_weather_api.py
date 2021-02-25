from configparser import ConfigParser
import requests
import json


class OpenWeatherAPI:

    def __init__(self, city):
        self.app_id = OpenWeatherAPI._fetch_app_id_from_credentials()
        self.api_endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.app_id}"
        self.api_response = None

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
        return f"It looks like this place has {weather_desc} today. Temperature is {temperature}"

    def orchestrate_flow(self):
        self._hit_api()
        temperature = self._parse_temperature_from_response()
        weather_desc = self._parse_weather_from_response()
        text = self._prepare_text_for_speech_engine(temperature, weather_desc)
        return text

