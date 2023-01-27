from playwright.sync_api import sync_playwright
from config import path

import pandas as pd
import json


def get_urls():
    df = pd.read_excel(f'{path}/templates/companies.xlsx')
    data_id = df[['Symbol', 'Exchange', 'My CODE', 'Company']]
    data_url = []
    for item in data_id.values.tolist():
        data_url.append({'url':f'https://www.morningstar.com/stocks/{item[1]}/{item[0]}/financials',
                         'Symbol': item[0],
                         'Exchange': item[1],
                         'My CODE': item[2],
                         'Company': item[3]})
    return data_url



def run(playwright, url):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    api = []
    page.on("request", lambda request: api.append(request.url))
    page.goto(url)
    company = page.text_content('h1.mdc-heading').strip().split('\n')[0].strip()
    browser.close()
    data = []
    for api_id in api:
        if 'api-global' in api_id:
            data.append({'id': api_id.split('/')[7], 'company': company})
    return data

with sync_playwright() as playwright:
    data = []
    for item in get_urls():
        id = run(playwright, item['url'])
        print(len(id))
        if len(id) > 0:
            id = dict(*id)
            print(id['id'], id['company'])
            data.append({'url':item['url'],
                        'Symbol': item['Symbol'],
                        'Exchange': item['Exchange'],
                        'id': id['id'],
                        'My CODE': item['My CODE'],
                        'Company': id['company']})
    
    with open('id.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)