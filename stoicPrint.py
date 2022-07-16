import requests
import json


def pullQuote():
    query = "https://stoic-quotes.com/api/quote"
    quote = requests.get(query)
    return quote.json()

def to_coloured(col):
    return f"\x1b[38;2;{col[0]};{col[1]};{col[2]}m"

data = pullQuote()

bold = "\033[1m"

print(bold + to_coloured((194,217,76)) + data.get("text") + \
        "\n - " + to_coloured((248,131,121)) + data.get("author"))