import urllib.request, json
from .models import Quote
import requests
url = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    """"""
    response = requests.get(url).json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote
