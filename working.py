import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    template = 'https://www.indeed.com/jobs?q={}l={}'
    url = template.format(position, location)
    return url

url = get_url('developer', 'salt lake city ut')
response = requests.get(url)

print(response)
