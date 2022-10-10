#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().system('pip install apify')


# In[9]:


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


# In[14]:


base_url = "https://www.realsimple.com/home-organizing/decorating"

page = requests.get(base_url)
data=[]


# In[15]:


response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[51]:


print(soup.prettify())


# In[16]:


list1 = soup.find('div',{"class" : "comp three-post__inner card-list mntl-document-card-list mntl-card-list mntl-block"})
list2 = list1.find_all('a')


# In[17]:


for title in list2:
    details = []
    details.append(title.find("div",{"class":"card__content"}).get("data-tag"))
    details.append(title.get("href")) #link to the article
    details.append(title.find('span',{"class":"card__title"}).contents[0].contents[0])
    details.append(title.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
    data.append(details)


# In[18]:


data


# In[26]:


links=soup.find("div",{"class":"comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block"})
a = links.find_all('a')
len(links)


# In[27]:


for atags in a:
    details = []
    details.append(atags.find("div",{"class":"card__content"}).get("data-tag"))
    details.append(title.get("href")) #link to the article
    details.append(atags.find('span',{"class":"card__title"}).contents[0].contents[0])
    details.append(atags.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
    data.append(details)
    count=count+1
    
    


# In[23]:


df = pd.DataFrame (data, columns = ['Category','Link','Title','Image_Link'])


# In[24]:


df


# In[32]:


from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_Q8Nb6XkPh9ZdZnhkYCZL7BgKB5ZZF531g2xb")

# Prepare the actor input
run_input = {
    "maxRequestsPerCrawl": 100,
    "extendOutputFunction": """async ({ data, item, product, images, fns, name, request, variants, context, customData, input, Apify }) => {
  return item;
}""",
    "extendScraperFunction": """async ({ fns, customData, Apify, label }) => {
 
}""",
    "customData": {},
    "maxConcurrency": 100,
    "maxRequestRetries": 3,
}

# Run the actor and wait for it to finish
run = client.actor("mshopik/dania-furniture-scraper").call(run_input=run_input)
list1=[]
# Fetch and print actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    list1.append(item)


# In[39]:


df1=pd.DataFrame(list1)


# In[44]:


df1


# In[45]:


df1=df1[['url','color','size','title','id','description','price','currency','product_type','images_urls','additional']]


# In[46]:


df1


# In[48]:


df1.to_excel("output.xlsx")


# In[49]:


df.to_excel("output1.xlsx")


# In[ ]:




