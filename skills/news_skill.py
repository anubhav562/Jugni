from newsapi import NewsApiClient
from configparser import ConfigParser


class NewsSkill:

    def __init__(self):
        api_key = self._fetch_api_key_from_credentials()
        self.new_api_client = NewsApiClient(api_key=api_key)

    @staticmethod
    def _fetch_api_key_from_credentials():
        config_parser = ConfigParser()
        config_parser.read("credentials.cfg")
        return config_parser.get("NewsAPI", "api_key")

    def orchestrate_flow(self):
        top_headlines = self.new_api_client.get_top_headlines(
            language="en", country="in"
        )
        first_three_articles = top_headlines["articles"][:10]
        list_of_text = ["Reading the news now"] + [article["title"] for article in first_three_articles]
        return list_of_text
