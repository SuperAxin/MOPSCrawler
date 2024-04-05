



from Spider import FinancialStatementFetcher

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    url = 'https://mops.twse.com.tw/server-java/t164sb01'
    types = 3
    coid = 2330
    year = 2020
    season = 1

    getter = FinancialStatementFetcher(url, types, coid, year, season)
    response_text = getter.send_request()
    table = getter.catch_table()
    print(table)

