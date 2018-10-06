import time
import urllib.request


def download(url, headers, num_retries=6):
    try:
        request = urllib.request.Request(url=url, headers=headers, timeout=10)
        response = urllib.request.urlopen(request)
        if response.get_code() == 200:
            print(response.info())
            return response.read().decode("utf-8")
    except Exception as e:
        if num_retries > 0:
            time.sleep(10)
            return download(url, headers, num_retries-1)


if __name__ == '__main__':
    url = "https://www.baidu.com"
    headers = {
        "User-Agent": ""
    }
    response = download(url, headers)

    print(response)