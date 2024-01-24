import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://cryptocurrencyjobs.co/?query=marketing').text # accept text only, bring text

# create beautiful soup instance
soup = BeautifulSoup(html_text, 'lxml') # lxml is the parser
jobs = soup.find_all('li', class_='ais-Hits-item')
print(jobs)