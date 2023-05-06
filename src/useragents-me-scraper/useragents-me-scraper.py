import json
import requests
from bs4 import BeautifulSoup

# Define saving of JSON


def _save_ua_cache():
    FILENAME = 'uacache.json'
    with open(FILENAME, 'w') as outfile:
        json.dump(ua_json, outfile)

# Define checking of existing JSON

# Define basic scraping/fetching of JSON

# Define main functionality of getting UA with specifications

# Check if there is an existing file
