
import requests
url = 'http://tinyurl.com/api-create.php?url='


def hello() -> str:
    return "Hello World!"


def shorten_url(long_url):
    response = requests.get(url + long_url)
    return response.text
