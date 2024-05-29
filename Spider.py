import requests
import pandas as pd

from bs4 import BeautifulSoup

class GetFinancialStatement:
    def __init__(self, url, types, coid, year, season): # types = [0:資產負債, 1:損益, 2:現金流量]
        self.url = url
        self.params = {
            'step': '1',
            'DEBUG': '',
            'CO_ID': str(coid),
            'SYEAR': str(year),
            'SSEASON': str(season),
            'REPORT_ID': 'C'
        }
        self.types = int(types)
        self.content = None

    def send_request(self):
        try:
            print(self.url)
            response = requests.post(self.url, params=self.params)
            print(response.content)
            print('==================================================================================================')
            if response.status_code == 200:
                print("Request successful")
                content = response.content
                # print(content)
                content = content.decode('big5')
                # print(content)
                self.content = content
                return None
            else:
                print("Request failed with status code:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

    def catch_table_old(self): # 2019年之前抓取特定表格抓取特定表格
        if self.content is not None:
            soup = BeautifulSoup(self.content, 'html.parser')

            #　篩選table
            table = soup.find_all('table')[self.types + 1]
            tr_list = table.find_all('tr')
            Chinese_text = []
            Money = []
            for tr in tr_list:
                td_list = tr.find_all('td')
                for td in td_list[0:1]: # 會計科目
                    text = td.text.strip()
                    Chinese_text.append(text)

                for td in td_list[1:2]: # 當季金額
                    number = td.text.strip()
                    Money.append(number)
            d = {
                'Accounts': Chinese_text,
                'Money': Money
            }

            df = pd.DataFrame(data=d)
            return df
        else:
            print("No content available. Please call send_request first.")
        return None
    def catch_table(self): # 2019年之後抓取特定表格
        if self.content is not None:
            soup = BeautifulSoup(self.content, 'html.parser')
            div_content = soup.find('div', class_='content')
            if div_content:
                tables = div_content.find_all('table')[self.types:self.types+1]  # 針對types的內容抓取table
                for table in tables:
                    rows = table.find_all('tr')[2:]  # 從第三個tr開始
                    Chinese_text = []
                    Money = []
                    for row in rows:
                        datas = row.find_all('td')[1:2]  # 只抓會計科目
                        for data in datas:
                            text = data.find('span', class_='zh').text.strip()
                            Chinese_text.append(text)
                        datas = row.find_all('td')[2:3]  # 只抓金額
                        for data in datas:
                            number = data.text
                            Money.append(number)

                    print(' ')
                    d = {
                        'Accounts': Chinese_text,
                        'Money': Money
                    }

                    df = pd.DataFrame(data=d)

            return df
        else:
            print("No content available. Please call send_request first.")
            return None

# Usage Example
'''url = 'https://mops.twse.com.tw/server-java/t164sb01'
types = 3
coid = 2330
year = 2020
season = 1

getter = FinancialStatementFetcher(url, types, coid, year, season)
response_text = getter.send_request()
table = getter.catch_table()
print(table)'''

