



from Spider import GET

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    url = "https://example.com"
    getter = GET(url)
    response_text = getter.send_request()
    if response_text:
        print_hi(response_text)

