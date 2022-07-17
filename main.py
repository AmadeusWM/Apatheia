import json
import random
import os

currDir = os.path.dirname(os.path.realpath(__file__))

def loadQuotes():
    with open (f'{currDir}/quotes.json', "r") as f:
        # Reading from file
        data = json.loads(f.read())
        return data

def to_coloured(col):
    return f"\x1b[38;2;{col[0]};{col[1]};{col[2]}m"

quotes = loadQuotes().get("quotes")

randomQuote = quotes[random.randrange(0, len(quotes))]

bold = "\033[1m"

print(bold + to_coloured((194,217,76)) + randomQuote.get("text") + \
        "\n - " + to_coloured((248,131,121)) + randomQuote.get("author"))