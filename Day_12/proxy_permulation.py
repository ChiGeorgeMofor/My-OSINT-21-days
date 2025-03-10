import requests

ip_addresses = [ "1.0.132.249:4153", "someproxy1.com:80",
"someproxy2.com:80", "someproxy3.com:80", "someproxy4.com:80",
"someproxy5.com:80", "someproxy6.com:80"]

url = 'https://cleantalk.org/blacklists/ivanov@gmail.com'

for proxy in ip_addresses: proxies = {'https': proxy}

try:
    response = requests.post(url, proxies=proxies)
    print(response.text)
except:
    print("No")