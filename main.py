



from Spider import FinancialStatementFetcher

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    url = 'https://mops.twse.com.tw/server-java/t164sb01'
    types = 3              # types = [0:資產負債, 1:綜合損益, 2:現金流量, 3:權益變動]
    coid = 2330
    year = 2020
    season = 1

    getter = FinancialStatementFetcher(url, types, coid, year, season)
    response_text = getter.send_request() # POST網址獲取資料
    table = getter.catch_table() # 資料清洗
    print(table)

