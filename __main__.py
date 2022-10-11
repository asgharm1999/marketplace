"""
Authors:
Muhammad Asghar masghar@andrew.cmu.edu 
Edvin Handoko ehandoko@andrew.cmu.edu 
Sahithya Senthilkumar sahithys@andrew.cmu.edu 
Saba Zaheer szaheer@andrew.cmu.edu
"""

#import installation_packages as ip
#packages = ['geopy', 'folium', 'apify', 'apify-client']
#for p in packages:
#    ip.import_or_install(p)

import pandas as pd
from tabulate import tabulate
import numpy as np
import os
import pip
import csv
import urllib3
import datetime
import glob
import aptdeco_scraper as aptd
import uhaul_scraper as uh
import craiglist_scraper as craigl
import dania_scraper as dania
import realsimple_dania_scraper as real
import etsy_scraper as etsy
import yellowpages_scraper as yp
import create_master_csv as master
import get_cached_data as cached
import re

# FUNCTIONS
def furniture():
    print('FURNITURES'.center(50, '-'))
    is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip()
    if is_cached != 'y':
        print("Gathering data, this will take some time.")

        # CRAIGSLIST
        craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
        df_craigslist = craigl.get_craigslist_search_results(craigslist_base_url)

        # DANIA
        df_dania = dania.get_dania_search_results(dania_token)

        # ETSY
        etsy_base_url = "https://www.etsy.com/search?q=furniture&page={page}&ref=pagination"
        df_etsy = etsy.get_etsy_search_results(etsy_base_url)

        # APTDECO
        aptdeco_base_url = "https://www.aptdeco.com/catalog/furniture?region=Northeast+%28NY%2C+NJ%2C+CT%2C+PA%2C+DE%29&page="
        df_aptdeco = aptd.get_aptdeco_search_results(aptdeco_base_url)
        
        # IKEA
        df_ikea = cached.get_cached_ikea()
        
    else:
        df_craigslist = cached.get_data_craigslist()
        df_dania = cached.get_data_dania()
        df_etsy = cached.get_data_etsy()
        df_aptdeco = cached.get_data_aptdeco()
        df_ikea = cached.get_data_ikea()
        
    df_furnitures = create_master(df_craigslist, df_dania, df_etsy, df_aptdeco, df_ikea)
    #show list of furniture based on the keyword
    furniture = input("What furniture would you like to browse?")
    columns = ('Post URL', 'Post Title', 'Price', 'Location')
    search_results = pd.DataFrame(columns=columns)
    for index, row in df_furnitures.iterrows():
        if re.search(furniture, row['Post Title']) != None:
            search_results.loc[len(search_results)] = row
    # df_furnitures.loc[re.search(pat, df_furnitures['Post Title']) != None]
    if search_results.empty:
        print("No furnitures found!")
    else:
        print(tabulate(search_results["Post URL":], headers = 'keys', tablefmt = 'simple', showindex=False))
    is_movers = input("Do you want to find nearest movers? (y/n)")
    if is_movers == 'y':
        movers()
        
def create_master(df1, df2, df3, df4, df5):
    # columns = ('Post URL', 'Post Title', 'Price', 'Location', 'Source')
    # df = pd.DataFrame(columns=columns)
    # print(df)
    
    # df1['Source'] = 'craigslist'
    # df1 = df1.loc[:,['Post URL', 'Post Title', 'Price', 'Location', 'Source']].copy()
    # print(df1)
    # df2['location'] = 'NA'
    # df2['source'] = 'dania'
    # df2 = df2.loc[:,['url', 'title', 'price', 'location', 'source']].copy()
    # print(df2)
    # df3['Location'] = 'NA'
    # df3['Post URL'] = 'NA'
    # df3['Source'] = 'etsy'
    # df3 = df3.loc[:,['Post URL', 'Title', 'Price', 'Location', 'Source']].copy()
    # print(df3)
    # df4['Source'] = 'aptdeco'
    # print(df4)
    # df5 = df5.loc[:,['post_url', 'post_title', 'price', 'location', 'source']].copy()
    
    # for index, row in df1.iterrows():
    #     df.loc[len(df)] = row
    # for index, row in df2.iterrows():
    #     df.loc[len(df)] = row
    # for index, row in df3.iterrows():
    #     df.loc[len(df)] = row
    # for index, row in df4.iterrows():
    #     df.loc[len(df)] = row
    # for index, row in df5.iterrows():
    #     df.loc[len(df)] = row
    
    # df = pd.concat([df1, df2, df3, df4, df5], axis=0, ignore_index=True)
    
    return df4
        
def visualizations():
    print("Visualizations")
    
def shops():
    print('NEAREST SHOPS'.center(50, '-'))
    location = input("Enter Location: ")
    is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip()
    if is_cached != 'y':
        # YELLOWPAGES
        yellowpages_base_url = "https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms="
        df_yellowpages = yp.get_yellowpages_search_results(yellowpages_base_url, location)
        if df_yellowpages.empty:
            print("No nearby movers!")
        else:
            print(tabulate(df_yellowpages, headers = 'keys', tablefmt = 'simple', showindex=False))
    else:
        df_yellowpages = cached.get_data_yellowpages()
        columns = ('Store URL', 'Name', 'Phone', 'Street_Address', 'Locality', 'Business_years')
        search_results = pd.DataFrame(columns=columns)
        for index, row in df_yellowpages.iterrows():
            if re.search(location, row['Locality']) != None:
                search_results.loc[len(search_results)] = row
        if search_results.empty:
            print("No nearby shops!")
        else:
            print(tabulate(search_results, headers = 'keys', tablefmt = 'simple', showindex=False))
    #redirect to map
    
def movers():
    print('NEAREST MOVERS'.center(50, '-'))
    zipcode = input('Enter Zipcode: ')
    is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip()
    if is_cached != 'y':
        # UHAUL
        uhaul_base_url = "https://www.uhaul.com/Locations/"
        df_uhaul = uh.get_uhaul_search_results(uhaul_base_url, zipcode)
        if df_uhaul.empty:
            print("No nearby movers!")
        else:
            print(tabulate(df_uhaul, headers = 'keys', tablefmt = 'simple', showindex=False))
    else:
        df_uhaul = cached.get_data_uhaul()
        columns = ('Store URL', 'Name', 'Location', 'Contact No', 'Operating Hours')
        search_results = pd.DataFrame(columns=columns)
        for index, row in df_uhaul.iterrows():
            if re.search(zipcode, row['Location']) != None:
                search_results.loc[len(search_results)] = row
        if search_results.empty:
            print("No nearby movers!")
        else:
            print(tabulate(search_results, headers = 'keys', tablefmt = 'simple', showindex=False))
    
def articles():
    print('ARTICLES'.center(50, '-'))
    is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip()
    if is_cached != 'y':
        # REALSIMPLE
        realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
        df_realsimple = real.get_realsimple_search_results(realsimple_base_url)
    else:
        df_realsimple = cached.get_data_realsimple()
    print(df_realsimple)


# MAIN MENU
print("INTRO".center(50, '-'))
print("Hello. It is recommended to use your terminal in fullscreen to view all the results.")
print("SETUP".center(50, '-'))
print("Please enter your Dania API token. View the Readme for instructions.")
dania_token = input()

df_furnitures = pd.DataFrame()
df_craigslist = pd.DataFrame()
df_dania = pd.DataFrame()
df_etsy = pd.DataFrame()
df_aptdeco = pd.DataFrame()
df_ikea = pd.DataFrame()

browse = True
while browse:
    print('MENU'.center(51, '-'))
    print('1. Search Furniture')
    print('2. View Visualizations')
    print('3. Explore Nearest Shops')
    print('4. Find Nearest Movers')
    print('5. Browse Articles')
    print('6. Exit')
        
    menu = input("Enter Menu: ")
    if(menu == '1'):
        furniture()
    elif(menu == '2'):
        visualizations()
    elif(menu == '3'):
        shops()
    elif(menu == '4'):
        movers()
    elif(menu == '5'):
        articles()
    elif(menu == '6'):
        browse = False
    else:
        print("Wrong Input, Try Again!")