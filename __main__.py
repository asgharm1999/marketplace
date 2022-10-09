import pandas as pd
import numpy as np
import os
import pip
import csv
import urllib3
import datetime
import glob
import get_scraped_data as sd
# import aptdeco_scraper as aptd
# import uhaul_scraper as uhaul
# import craiglist_scraper as craigl
# import realsimple_scraper as real
import etsy_scraper as etsy
# import yellowpages_scraper as yellow
# from apify_client import ApifyClient






print("Hello. It is recommended to use your terminal in fullscreen to view all the results.")
is_cached = input("Do you want to use cached date? This will not run BeautifulSoup code for new data (y/n)").lower().strip() == 'y'

if is_cached != 'y':
    sd.get_etsy_data
# use cached code
else:





