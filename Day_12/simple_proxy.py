#
import requests

proxies = {
    'https': '1.0.132.249:4153',
}

url = 'https://cleantalk.org/blacklists/ivanov@gmail.com'

response = requests.post(url, proxies=proxies)

print(response.text)