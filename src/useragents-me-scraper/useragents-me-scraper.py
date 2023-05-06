import json
import requests
from bs4 import BeautifulSoup

# Define saving of JSON


def _save_ua_cache(ua_processed_json):
    FILENAME = 'uacache.json'
    with open(FILENAME, 'w') as outfile:
        json.dump(ua_processed_json, outfile)

# Define checking of existing JSON


def _check_existing_ua_cache():
    existing_flag = True
    try:
        f = open('uacache.json')
    except:
        print('A local ua_cache file does not exist.')
        existing_flag = False
    return existing_flag
# Define basic scraping/fetching of JSON

# Define main functionality of getting UA with specifications

# Check if there is an existing file
