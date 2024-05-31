## MOPSCrawler - 公開資訊觀測站爬蟲 ##
MOPSCrawler是一個專門用於爬取台灣公開資訊觀測站( MOPS ) 中各公司財務報表的爬蟲程式，此程式使用 Python 編寫，借助 requests 庫發送網絡請求，以獲取 MOPS 網站上的財務報表頁面。並使用 BeautifulSoup 庫對頁面進行解析，提取所需的財務報表數據。最後再使用 pandas 庫將數據存儲為 DataFrame 格式，以便進一步分析和處理。

該爬蟲程式只需輸入指定公司的 CO_ID（公司ID）、年份（year）和季度（season），就可獲取特定公司特定年份季度的財務報表數據。
