from Spider import GetFinancialStatement


if __name__ == '__main__':
    url = 'https://mops.twse.com.tw/server-java/t164sb01'
    types = 0              # types = [0:資產負債, 1:綜合損益, 2:現金流量]
    coid = 2330            # COID 公司股票代碼
    year = 2020            # YEAR 財報年分
    season = 1             # SEASON 財報季度

    getter = GetFinancialStatement(url, types, coid, year, season)
    response_text = getter.send_request() # POST網址獲取資料
    table = getter.catch_table() # 資料清洗
    print(table)

