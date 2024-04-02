import requests

class GET:
    def __init__(self, url):
        self.url = url

    def send_request(self):
        try:
            response = requests.get(self.url)
            # 檢查是否成功收到回應
            if response.status_code == 200:
                print("Request successful")
                return response.text
            else:
                print("Request failed with status code:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

# 使用範例
url = "https://mops.twse.com.tw/mops/web/index"
getter = GET(url)
response_text = getter.send_request()
if response_text:
    print(response_text)