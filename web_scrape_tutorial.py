
#! Webscrape Job Board (Data Science)

#? Crypto Marketing vs Jr. Developer

#* Problem: How to search/apply Crypto Marketing jobs while monitoring Developer opportunities/requirements

# Crypto Marketing:
    # Specific Position (Marketing Lead, Growth Marketing Manager, etc.)
    # Salary
    # Remote
    # Full/Part Time

# Developer/Enginner
    # Requirements
    # Job Description
    # Salary
    # Location

#* Collect Data

# Public vs. Private
# Clean vs. Dirty

# Goal: Clean, Public data
    # Kaggle, Google, data.gov, data.world, github

# Backup: Clean, Private data
    # APIs: Use Python, contact server, request data
    # Usually has authentication process
    # TODO: Python for Everybody (Network Programming -> Using Web Services)

# Third: Unclean, Private data
    # Can be pretty common

# Last: Public, Not Clean data
    # Web scraping / web crawling
    # Collect job data around job postings

# TODO: Start Small

# 0. Use burner account
# 1. Log in with login information
# 2. Navigate to job search page
    # 2a. Search for crypto jobs
    # 2b. Search for python developer jobs
# 3. Go through and select each job posting (for loop?) in order to scrape wanted job data
# 4. Once all entries on page cycled through, select next page and repeat process for all remaining pages
# 5. Save all data to daily csv file
# 6. Run every night (cronjob)

#? Problems:
# -Throttle speed to avoid detection
    # -Took up to half a day to scrape all
# -Limit of # of jobs possible to scrape (total jobs vs. amount in pages)
# -Log into (sample_website) daily


#! Webscrape Job Board( Izzy Analytics)

#* 1. Import Modules

# import bs4, requests
# (beautiful soup, requests)

import csv  # export the data
from datetime import datetime   # get current date
import requests # send get request to server to get raw html
from bs4 import BeautifulSoup   # parse html, extract data we want

#* 2. Survey Page Content/Structure

# Think about what data you want to extract from each job

# Ex. job title, company, post date, job summary, salary range

#* 3. How to Page Through Results

# Replicate same kind of search through a python request
    # Hint: look at url
        # Query being performed by server is encoded in the url
            # ?q= indicates start of the query
            # l= indicates where, location
            # Additional search query data (click on filters, see how it updates url)
# Copy everythin up to vjk
    # Use this as template to create url when performing Python searches

template = 'https://www.indeed.com/jobs?q=marketing&l=Salt+Lake+City%2C+UT'

# Delete job text and replace with curly braces

new_template = 'https://www.indeed.com/jobs?q={}l={}}'

# Creates a string template where we can insert any job position or location we want

def get_url(position, location):
    template = 'https://www.indeed.com/jobs?q={}l={}}'

# Use string formatting to pass in position/location and assign to variable url
    
def get_url(position, location):
    template = 'https://www.indeed.com/jobs?q={}l={}}'
    url = template.format(position, location)
    return url

# Use new get_url function to assign return value to a url variable
# Pass in position, location

url = get_url('developer', 'salt lake city ut')

#* 4. Send get request to website and extract raw html

# Returns a response object

response = requests.get(url)
# sends request to site, response will be sent back
# if successful, response object returns 200 code

#* 5. Extract Raw HTML

# Extract raw html from response object with text attribute
# Parse with beautiful soup to create soup object
    # Use to navigate html tree structure, extract relevant parts
    # Use html.parser as second argument

def get_url(position):
    template = 'https://cryptocurrencyjobs.co/?query={}'
    url = template.format(position)
    return url

url = get_url('marketing')

response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')  # extracts text 

# Identify something unique about a job record that enables us to extract all job records as a collection

#* Use Inspector

# Find html tag that encloses whole record
# Find way to identify it uniquely amongst all other similar tags
    # div is generic, look for class name or id.
# If extact all div tags with this class, should have collection of objects that represent job postings on this page

def get_url(position):
    template = 'https://cryptocurrencyjobs.co/?query={}'
    url = template.format(position)
    return url

url = get_url('marketing')

response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

cards = soup.find_all('div','grid text-sm')
# find all div tags that have specified class name
# will return list of all elements that meet this search criteria
