# The aim of this code is to scrape the title(header) of a specific web page and print it out.

import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/project/duckduckgo-search/"

web_page = requests.get(url)

soup = BeautifulSoup(web_page.content, "html.parser")


# Using CSS-selectors to find elements on a web page 
header = soup.find("h1").get_text()

print(header)