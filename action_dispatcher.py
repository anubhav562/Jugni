from skills.camera_skill import CameraSkill
from skills.open_weather_api import OpenWeatherAPI
from skills.google_maps_skill import GoogleMaps
from skills.jokes_skill import JokeSkill

from behaviour.terminate_jugni import TerminateJugni
from behaviour.actions_guide import ActionsGuide

intent_to_skill_mapping = {
    "getWeather": OpenWeatherAPI,
    "cameraApplication": CameraSkill,
    "getDirections": GoogleMaps,
    "joke": JokeSkill,
    "terminate": TerminateJugni,
    "actionsGuide": ActionsGuide
}
