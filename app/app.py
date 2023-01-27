import httpx
import json

from loguru import logger

from config import headers, params
from config import path
from models.Enquiry_1 import Enquiry_one
from models.Enquiry_2 import Enquiry_two
from models.Enquiry_3 import Enquiry_three
from models.Enquiry_4 import Enquiry_four
from models.Enquiry_5 import Enquiry_five
from models.Enquiry_6 import Enquiry_six


from xlsx import make_xlsx


logger.add(f'{path}/error.log', format='{time} {level} {message}', level='DEBUG', serialize=False)


def response(url: str = 'https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/0P000002X8/incomeStatement/detail'):
    return httpx.get(url, headers=headers, params=params, timeout=5.0)


def parsing_data():
    with open(f'{path}/id.json', 'r') as json_file:
        data_json = json.loads(json_file.read())
        data_xlsx = []
        id = 1
        for item in data_json:
            print(item["id"], '================', item["Company"])
            if item["id"] is not None:
                enquiry_url = {'incomeStatement': f'https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/{item["id"]}/incomeStatement/detail',
                'balanceSheet': f'https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/{item["id"]}/balanceSheet/detail',
                'OperatingAndEfficiency': f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/OperatingAndEfficiency/{item["id"]}',
                'financialHealth': f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/financialHealth/{item["id"]}',
                'cashFlow': f'https://api-global.morningstar.com/sal-service/v1/stock/keyStats/cashFlow/{item["id"]}',
                'dividends': f'https://api-global.morningstar.com/sal-service/v1/stock/dividends/v4/{item["id"]}/data'}
                try:
                   enquiry_one = Enquiry_one(response(url=enquiry_url['incomeStatement']).content).dict()
                except:
                    enquiry_one = {}
                    enquiry_one = Enquiry_one(response(url=enquiry_url['incomeStatement']).content).dict()
                    print(item["id"], 'enquiry#1 error', item["url"])
                try:
                    enquiry_two = Enquiry_two(response(url=enquiry_url['balanceSheet']).content).dict()
                except:
                    enquiry_two = {}
                    enquiry_two = Enquiry_two(response(url=enquiry_url['balanceSheet']).content).dict()
                    print(item["id"], 'enquiry#2 error', item["url"])
                try:
                    enquiry_three = Enquiry_three(response(url=enquiry_url['OperatingAndEfficiency']).content).dict()
                except:
                    enquiry_three = {}
                    print(item["id"], 'enquiry#3 error', item["url"])
                try:
                    enquiry_four = Enquiry_four(response(url=enquiry_url['financialHealth']).content).dict()
                except:
                    enquiry_four = {}
                    print(item["id"], 'enquiry#4 error', item["url"])
                try:
                    enquiry_five = Enquiry_five(response(url=enquiry_url['cashFlow']).content).dict()
                except:
                    enquiry_five = {}
                    print(item["id"], 'enquiry#5 error', item["url"])
                try:
                    enquiry_six = Enquiry_six(response(url=enquiry_url['dividends']).json()).dict()
                except:
                    enquiry_six = {}
                    print(item["id"], 'enquiry#6 error', item["url"])
                data_xlsx.append({'Enquiry#1': enquiry_one,
                                  'Enquiry#2': enquiry_two,
                                  'Enquiry#3': enquiry_three,
                                  'Enquiry#4': enquiry_four,
                                  'Enquiry#5': enquiry_five,
                                  'Enquiry#6': enquiry_six,
                                  "Symbol": item["Symbol"],
                                  "Exchange": item["Exchange"],
                                  "My CODE": item["My CODE"],
                                  'Company': item['Company']})
            # if id == 11:
            #     break
            id +=1
    make_xlsx(data_xlsx)
@logger.catch
def main():
    parsing_data()

if __name__ == "__main__":
    main()