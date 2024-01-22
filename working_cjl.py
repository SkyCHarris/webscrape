# URL: https://cryptojobslist.com/remote_marketing

import csv  # export the data
from datetime import datetime   # get current date
import requests # send get request to server to get raw html
from bs4 import BeautifulSoup   # parse html, extract data we want

# Get url for specified position
def get_url(location, position):
    template = 'https://cryptojobslist.com/{}_{}'
    url = template.format(location, position)
    return url

# url variable
url = get_url('remote', 'marketing')

response = requests.get(url)    # get response from webpage

print(response) # check if response successful  (100, 200, 400 codes)

soup = BeautifulSoup(response.text, 'html.parser')  # extracts text

cards = soup.find_all('li', li_='JobInline_job__n_Spc')

print(len(cards))
