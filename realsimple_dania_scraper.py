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
from apify_client import ApifyClient
import pip

def get_realsimple_search_results(base_url, token):
    
    def import_or_install(package):
    try:
        __import__(package)
    except:
        pip.main(['install', package])       

    # Required for RealSimple
    packages = ['apify', 'apify-client']
    for p in packages:
        import_or_install(p)
        
    page = requests.get(base_url)
    data=[]

    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.prettify())

    list1 = soup.find('div',{"class" : "comp three-post__inner card-list mntl-document-card-list mntl-card-list mntl-block"})
    list2 = list1.find_all('a')

    for title in list2:
        details = []
        details.append(title.find("div",{"class":"card__content"}).get("data-tag"))
        details.append(title.get("href")) #link to the article
        details.append(title.find('span',{"class":"card__title"}).contents[0].contents[0])
        details.append(title.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
        data.append(details)
    
    # print(data)

    links = soup.find("div",{"class":"comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block"})
    a = links.find_all('a')
    len(links)

    for atags in a:
        details = []
        details.append(atags.find("div",{"class":"card__content"}).get("data-tag"))
        details.append(title.get("href")) #link to the article
        details.append(atags.find('span',{"class":"card__title"}).contents[0].contents[0])
        details.append(atags.find('div',{"class":"img-placeholder"}).find('img').get("data-src"))
        data.append(details)
        # count = count + 1
    

    df = pd.DataFrame (data, columns = ['Category','Link','Title','Image_Link'])
    # print(df)

    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'RealSimple Results ({timestamp}).csv', index=False)

    # Initialize the ApifyClient with your API token
    client = ApifyClient(token)

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
    
    df1 = pd.DataFrame(list1)
    # print(df1)
    df1 = df1[['url','color','size','title','id','description','price','currency','product_type','images_urls','additional']]
    df1.to_csv(f'Dania Results ({timestamp}).csv', index=False)