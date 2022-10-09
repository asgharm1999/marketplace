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


print("Hello. It is recommended to use your terminal in fullscreen to view all the results.")
print("Please enter your RealSimple API token. View the Readme for instructions.")
realsimple_token = input()
is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip() == 'y'

if is_cached != 'y':
    print("Gathering data, this will take some time.")

    # CRAIGSLIST
    craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
    craigl.get_craigslist_search_results(craigslist_base_url)

    # REALSIMPLE & DANIA 
    realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
    real.get_realsimple_search_results(realsimple_base_url, realsimple_token)

    # ETSY
    etsy_base_url = "https://www.etsy.com/search?q=furniture&page={page}&ref=pagination"
    etsy.get_etsy_search_results(etsy_base_url)

    # APTDECO
    aptdeco_base_url = 
    aptd.get_aptdeco_search_results(aptdeco_base_url)

    # YELLOWPAGES
    yellowpages_base_url = 
    yp.get_yellowpages_search_results(yellowpages_base_url)

    # UHAUL
    uhaul_base_url = 
    uh.get_uhaul_search_results(uhaul_base_url)


    if realsimple_token.len > 1:
        master.create_master_csv(craigslist, realsimple, dania, etsy, yellowpages, uhaul, aptdeco)
    else: 
        master.create_master_csv(craigslist, dania, etsy, yellowpages, uhaul, aptdeco)

# use cached code
else:
    cached.get_cached_data(craigslist, realsimple, dania, etsy, yellowpages, uhaul, aptdeco)

exit = input()
# if keyboard interrupt with exit, stop program
if exit:
    exit
else 
    ps.browse()