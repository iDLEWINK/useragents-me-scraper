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


def _is_existing_ua_cache():
    existing_flag = True
    try:
        f = open('ua_cache.json')
        f.close()
    except:
        print('A local ua_cache.json file does not exist.')
        existing_flag = False
    return existing_flag


def _is_outdated_ua_cache():
    outdated_flag = True
    try:
        f = open('ua_cache.json')
        ua_data = json.load(f)
        outdated_flag = utils.is_outdated(ua_data['end_date'])
        if(outdated_flag):
            print('ua_cache is outdated. Awaiting to scrape a new one.')
        f.close()
    except:
        print('An exception concerning the ua_cache.json file has occurred.')
    return outdated_flag
# Define basic scraping/fetching of JSON


def _scrape_ua_me():
    URL = "https://www.useragents.me/"
    r = requests.get(URL)

    content = BeautifulSoup(r.content, 'html5lib')

    common_div = content.find(id="most-common-desktop-useragents-json-csv")
    common_user_agents = common_div.div.textarea.string
    ua_raw_json = json.loads(common_user_agents)

    return ua_raw_json

# Define processing of raw UA data by adding start_date, end_date, and content key


def _process_ua(ua_raw_json):
    start_date = utils.date.today()
    end_date = start_date + utils.timedelta(days=7)

    ua_processed_json = {
        "start_date": str(start_date),
        "end_date": str(end_date),
        "content": ua_raw_json
    }

    return ua_processed_json

# Define main functionality of getting UA with specifications


def get_uas():
    retrieved_uas = []

    # If cache does not exist or is outdated
    if not _is_existing_ua_cache() or _is_outdated_ua_cache():
        # Process/Format
        ua_raw_json = _scrape_ua_me()
        ua_processed_json = _process_ua(ua_raw_json)
        # Save
        _save_ua_cache(ua_processed_json)
        print('Useragents.me scraped commenced.')

    # Loading the file
    with open('ua_cache.json', 'r') as f:
        print('Reading files...')
        ua_data = json.load(f)

    retrieved_uas = ua_data['content']
    print(str(len(retrieved_uas)), 'useragents successfully retrieved.')

    return retrieved_uas
