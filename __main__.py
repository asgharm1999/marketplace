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
import realsimple_dania_scraper as real
import etsy_scraper as etsy
import yellowpages_scraper as yp
import create_master_csv as master
import get_cached_data as cached
import prompts as ps
from apify_client import ApifyClient

def furniture():
    print('Search Furniture: ')
    furniture = input()
    
def shops():
    print('Enter Zipcode: ')
    zipcode = input()
    
def movers():
    print('Enter Zipcode: ')
    zipcode = input()
    
def articles():
    print('LIST OF ARTICLES')
    
def create_master_csv(craigslist, dania, etsy, yellowpages, uhaul, aptdeco, realsimple={}):
    print('')

def get_cached_data(craigslist, dania, etsy, yellowpages, uhaul, aptdeco, realsimple):
    print('')

print("INTRO".center(50, '-'))
print("Hello. It is recommended to use your terminal in fullscreen to view all the results.")
print("SETUP".center(50, '-'))
print("Please enter your RealSimple API token. View the Readme for instructions.")
realsimple_token = input()
is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip() == 'y'

if is_cached != 'y':
    print("Gathering data, this will take some time.")

    # CRAIGSLIST
    craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
    craigslist = craigl.get_craigslist_search_results(craigslist_base_url)

    # REALSIMPLE & DANIA 
    realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
    realsimple = real.get_realsimple_search_results(realsimple_base_url, realsimple_token)

    # ETSY
    etsy_base_url = "https://www.etsy.com/search?q=furniture&page={page}&ref=pagination"
    etsy = etsy.get_etsy_search_results(etsy_base_url)

    # APTDECO
    aptdeco_base_url = "https://www.aptdeco.com/catalog/furniture?region=Northeast+%28NY%2C+NJ%2C+CT%2C+PA%2C+DE%29&page="
    aptdeco = aptd.get_aptdeco_search_results(aptdeco_base_url)

    # YELLOWPAGES
    yellowpages_base_url = "https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms="
    yellowpages = yp.get_yellowpages_search_results(yellowpages_base_url)

    # UHAUL
    uhaul_base_url = "https://www.uhaul.com/Locations/"
    uhaul = uh.get_uhaul_search_results(uhaul_base_url)
    
    dania = "To be defined"

    if realsimple_token.len > 1:
        master.create_master_csv(craigslist, dania, etsy, yellowpages, uhaul, aptdeco, realsimple)
    else: 
        master.create_master_csv(craigslist, dania, etsy, yellowpages, uhaul, aptdeco)

# use cached code
else:
    cached.get_cached_data(craigslist, realsimple, dania, etsy, yellowpages, uhaul, aptdeco)

play = True
while play:
    print('MENU'.center(51, '-'))
    print('1. Search Furniture')
    print('2. Explore Nearest Shops')
    print('3. Find Nearest Movers')
    print('4. Browse Articles')
    print('5. Exit')
    
    menu = input()
    if(menu == 1):
        furniture()
    elif(menu == 2):
        shops()
    elif(menu == 3):
        movers()
    elif(menu == 4):
        articles()
    elif(menu == 5):
        play = False
    else:
        print("Wrong Input, Try Again!")
    
exit = input()
# if keyboard interrupt with exit, stop program
if exit:
    exit
else:
    ps.browse()