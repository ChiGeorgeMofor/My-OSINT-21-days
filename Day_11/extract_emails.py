# The aim of this code is to scrape a webpaege(cleantalk.org) and extract email addresses from the page using regular expressions.
import requests
import re # re module, provides functions for working with regular expressions.

url = "https://cleantalk.org//blacklists/mofor@gmail.com"

html = requests.get(url).text

result = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", html)

print(result)