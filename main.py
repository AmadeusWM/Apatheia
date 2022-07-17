import json
import os
from datetime import date

CURRDIR = os.path.dirname(os.path.realpath(__file__))
YELLOW = (194,217,76)
PINKISH = (248,131,121)

def loadQuotes():
    with open (f'{CURRDIR}/quotes.json') as f:
        # Reading from file
        data = json.load(f)
        return data

def to_coloured(col):
    return f"\x1b[38;2;{col[0]};{col[1]};{col[2]}m"

quotes = loadQuotes().get("quotes")

curr_date = date.today()
randomQuote = quotes[(curr_date.day + curr_date.month + curr_date.year) % len(quotes)]

bold = "\033[1m"

print(bold + to_coloured(YELLOW) + randomQuote.get("text") + \
        "\n- " + to_coloured(PINKISH) + randomQuote.get("author"))