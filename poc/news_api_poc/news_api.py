"""
Rough file for playing around with the API
"""
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='e0768fdf13ad4efc8bc2abc78343a41d')

top_headlines = newsapi.get_top_headlines(
    language="en", country='in'
)

print(top_headlines)
