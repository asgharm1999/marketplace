import installation_packages as ip
packages = ['geopy', 'folium', 'apify', 'apify-client']
for p in packages:
    ip.import_or_install(p)

import pandas as pd
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
import realsimple_scraper as real
import dania_scraper as dania
import etsy_scraper as etsy
import yellowpages_scraper as yp
import get_cached_data as cached
import install_packages as ip
    
def furniture():
    print('FURNITURES'.center(50, '-'))
    furniture = input("What furniture would you like to browse?")
    #show list of furniture based on the keyword
    is_movers = input("Do you want to find nearest movers? (y/n)")
    if is_movers == 'y':
        movers()
        
def visualizations():
    print("Visualizations")
    minimum_price = input("Minimum Price: ")
    maximum_price = input("Maximum Price: ")
    minimum_rating = input("Minimum Rating: ")
    #call the visualization
    
def shops():
    print('NEAREST SHOPS'.center(50, '-'))
    zipcode = input("Enter Zipcode: ")
    #show list of shops in the particular zipcode
    
def movers():
    print('NEAREST MOVERS'.center(50, '-'))
    zipcode = input('Enter Zipcode: ')
    #show list of shops in the particular zipcode
    
def articles():
    print('ARTICLES'.center(50, '-'))
    #show list of articles

print("INTRO".center(50, '-'))
print("Hello. It is recommended to use your terminal in fullscreen to view all the results.")
print("SETUP".center(50, '-'))
print("Please enter your Dania API token. View the Readme for instructions.")
dania_token = input()
is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip() == 'y'

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

    # YELLOWPAGES
    yellowpages_base_url = "https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms="
    df_yellowpages = yp.get_yellowpages_search_results(yellowpages_base_url)

    # UHAUL
    uhaul_base_url = "https://www.uhaul.com/Locations/"
    df_uhaul = uh.get_uhaul_search_results(uhaul_base_url)
    
    # REALSIMPLE
    realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
    df_realsimple = real.get_realsimple_search_results(realsimple_base_url)

# use cached code
else:
    df_craiglist = cached.get_cached_craiglist()
    df_dania = cached.get_cached_dania()
    df_etsy = cached.get_cached_etsy()
    df_aptdeco = cached.get_cached_aptdeco()
    df_yellowpages = cached.get_cached_yellowpages()
    df_uhaul = cached.get_cached_uhaul()
    df_realsimple = cached.get_cached_realsimple()

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
    if(menu == 1):
        furniture()
    elif(menu == 2):
        visualizations()
    elif(menu == 3):
        shops()
    elif(menu == 4):
        movers()
    elif(menu == 5):
        articles()
    elif(menu == 6):
        browse = False
    else:
        print("Wrong Input, Try Again!")

# exit = input()
# if keyboard interrupt with exit, stop program
# if exit:
#    exit
# else:
#    browse()