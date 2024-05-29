from Spider import GetFinancialStatement


if __name__ == '__main__':
    url = 'https://mops.twse.com.tw/server-java/t164sb01'
    types = input('請輸入財報種類... e.x. 0:資產負債, 1:綜合損益, 2:現金流量 :') # types = [0:資產負債, 1:綜合損益, 2:現金流量]
    coid = input('請輸入股票代碼... e.x.2330 :')     # COID 公司股票代碼
    year = input('請輸入公司年分... e.x.2020 :')     # YEAR 財報年分
    season = input('請輸入季度... e.x. 1 :')       # SEASON 財報季度

    getter = GetFinancialStatement(url, types, coid, year, season)
    response_text = getter.send_request() # POST網址獲取資料
    if int(year) > 2019:
        table = getter.catch_table()
    else:
        table = getter.catch_table_old() # 資料清洗
    table.to_csv('New_Data.csv')
    print(table)

