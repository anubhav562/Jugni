import webbrowser
import random

TEMPLATED_RESPONSES_1 = [
    "Showing the directions to {destination}",
    "The directions to {destination} are on your screen.",
    "Fetched the directions to {destination}.",
    "Here are the directions to {destination}.",
    "Showing directions to {destination} on google maps now."
]

TEMPLATED_RESPONSES_2 = [
    "Showing the directions from {origin} to {destination}",
    "The directions from {origin} to {destination} are on your screen.",
    "Now, showing you the directions from {origin} to {destination}.",
    "Here are the directions from {origin} to {destination}.",
    "Showing directions from {origin} to {destination} on google maps now."
]


class GoogleMaps:
    def __init__(self, origin=None, destination=None, travelMode=None):
        self.origin = origin
        self.destination = destination
        self.travel_mode = travelMode
        self.google_maps_url = self._prepare_search_query_string()
        self.google_chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

    def _prepare_search_query_string(self):

        base_url = "https://www.google.com/maps/dir/?api=1"
        if self.origin:
            base_url = base_url + f"&origin={self.origin}"
        if self.destination:
            base_url = base_url + f"&destination={self.destination}"
        if self.travel_mode:
            base_url = base_url + f"&travelmode={self.travel_mode}"

        return base_url

    def orchestrate_flow(self):

        if not self.origin and not self.destination:
            return "Sorry, I did not understand the request!"

        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(self.google_chrome_path))
        webbrowser.get("chrome").open_new_tab(self.google_maps_url)

        if self.origin:
            response = TEMPLATED_RESPONSES_2[random.randint(0, len(TEMPLATED_RESPONSES_2)-1)].format(
                destination=self.destination, origin=self.origin
            )
        else:
            response = TEMPLATED_RESPONSES_1[random.randint(0, len(TEMPLATED_RESPONSES_1) - 1)].format(
                destination=self.destination
            )

        return response
