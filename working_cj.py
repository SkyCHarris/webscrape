# URL: https://crypto.jobs/jobs?search=marketing&location=Remote

import csv  # export the data
from datetime import datetime   # get current date
import requests # send get request to server to get raw html
from bs4 import BeautifulSoup   # parse html, extract data we want

# Get url for specified position
def get_url(location, position):
    template = 'https://crypto.jobs/jobs?search={}&location={}'
    url = template.format(position, location)
    return url

# url variable
url = get_url('marketing', 'remote')

response = requests.get(url)    # get response from webpage

print(response) # check if response successful  (100, 200, 400 codes)

soup = BeautifulSoup(response.text, 'html.parser')  # extracts text

cards = soup.find_all('a class', 'job-url')

print((cards))
