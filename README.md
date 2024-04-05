這份程式是一個用於爬取 MOPS（Market Observation Post System）中各公司財務報表的爬蟲程式，此程式使用 Python 編寫，借助 requests 庫發送網絡請求，以獲取 MOPS 網站上的財務報表頁面。然後，使用 BeautifulSoup 庫對頁面進行解析，提取所需的財務報表數據。最後，使用 pandas 庫將數據存儲為 DataFrame 格式，以便進一步分析和處理。
該爬蟲程式支持指定公司的 CO_ID（公司ID）、年份（year）和季度（season），可以獲取特定公司特定年份季度的財務報表數據。使用者只需提供相應的參數，即可輕鬆獲取所需的財務報表信息。
