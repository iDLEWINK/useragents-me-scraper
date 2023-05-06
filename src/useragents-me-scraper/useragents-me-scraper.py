import json
import requests
import utils
from bs4 import BeautifulSoup

# Define saving of JSON


def _save_ua_cache(ua_processed_json):
    FILENAME = 'ua_cache.json'
    with open(FILENAME, 'w') as outfile:
        json.dump(ua_processed_json, outfile)

# Define checking of existing JSON


def _check_existing_ua_cache():
    existing_flag = True
    try:
        f = open('ua_cache.json')
    except:
        print('A local ua_cache.json file does not exist.')
        existing_flag = False
    return existing_flag

# Define basic scraping/fetching of JSON


def _scrape_ua_me():
    URL = "https://www.useragents.me/"
    r = requests.get(URL)

    content = BeautifulSoup(r.content, 'html5lib')

    common_div = content.find(id="most-common-desktop-useragents-json-csv")
    common_user_agents = common_div.div.textarea.string
    ua_raw_json = json.loads(common_user_agents)

    return ua_raw_json

# Define main functionality of getting UA with specifications
