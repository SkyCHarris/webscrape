# URL: https://cryptocurrencyjobs.co/?query=marketing

import csv  # export the data
from datetime import datetime   # get current date
import requests # send get request to server to get raw html
from bs4 import BeautifulSoup   # parse html, extract data we want

# Get url for specified position
def get_url(position):
    template = 'https://cryptocurrencyjobs.co/?query={}'
    url = template.format(position)
    return url

# url variable
url = get_url('marketing')

response = requests.get(url)    # get response from webpage

print(response) # check if response successful  (100, 200, 400 codes)

soup = BeautifulSoup(response.text, 'html.parser')  # extracts text

cards = soup.find_all('li', class_='ais-')  #TODO: Troubleshoot this. Try different job posting website

print(len(cards))

