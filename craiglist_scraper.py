#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
from bs4 import BeautifulSoup
import urllib3
import requests
import time
import re
import os
import math


# In[2]:


base_url = "https://pittsburgh.craigslist.org/search/fua"

page = requests.get(base_url)


# In[3]:


print(page.content)


# In[4]:


soup = BeautifulSoup(page.content, "html.parser")

total_results = int(soup.find('span', 'totalcount').text)
print(total_results)

total_pages = (total_results // 120) + 1

search_results = []


# In[5]:


# results_row = soup.find(class_="rows")

results = soup.find('ul', {'id': 'search-results'})
results_row = results.find_all('li', 'result-row')

print(results.prettify())


# In[6]:


# furniture_elems = results.find_all('li', class_="result-row")
# for furniture_elem in furniture_elems:
#     print(furniture_elem.text)
#     url = furniture_elem.find('a', class_="result-image gallery")['href']

# changed to process 5 pages instead of total_pages
for i in range(0, 6):
    
    params = {
        's': i*120        
    }

    response = requests.get(base_url, params=params)
    print('Processing Page {0}'.format(i+1))

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find('ul', {'id': 'search-results'})
    result_rows = results.find_all('li', 'result-row')

    for result_row in results_row:
        post_datetime = result_row.time['datetime']
        post_id = result_row.h3.a['data-id']
        post_url = result_row.h3.a['href']
        price = result_row.find('span', 'result-price').text
        location = result_row.find('span', 'result-hood').text if result_row.find('span', 'result-hood') else ''
        post_title = result_row.h3.a.text
    # post_title = furniture_elem.find('a', class_="result-title hdrlnk")

        search_results.append([
            post_datetime, post_id, post_url, price, location, post_title
        ])

        time.sleep(1)

    columns = ('Post Date', 'Post Id', 'Post URL', 'Price', 'Location', 'Post Title')
    df = pd.DataFrame(search_results, columns=columns)
    
#     print(price_elem.text.strip())
#     print(location_elem)
#     print(title_elem)
#     print(url_elem)
#     print(price_elem.text.strip())
#     print()


# In[8]:


print(df)


# In[9]:


timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
df.to_csv(f'Craigslist Results ({timestamp}).csv', index=False)


# In[10]:


# FURNITURE_URL = 'https://pittsburgh.craigslist.org/fuo/d/murrysville-lift-recliner/7534553122.html'
# furniture_page = requests.get(FURNITURE_URL)
# furniture_soup = BeautifulSoup(furniture_page.content, 'html.parser')


# In[11]:


# attributes = furniture_soup.find_all('p', class_='attrgroup')


# In[12]:


# for attribute in attributes:
#     spans = attribute.find_all('span')
#     for span in spans:
#         text = span.text.strip()
#         print(text)


# In[13]:


# posting_body = furniture_soup.find('section', {"id":"postingbody"})
# print(posting_body.text)

