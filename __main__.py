import pandas as pd
import numpy as np
import aptdeco_scraper as aptd
import uhaul_scraper as uhaul
import craiglist_scraper as craigl
import etsy_scraper as etsy
import yellowpages_scraper as yellow


print("It is recommended you use your terminal in fullscreen to view all the results.")
product_interest = input("What furniture would you like to browse:")
print("We found this: " + craigslist)

craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"

craigl.get_craigslist_search_results(craigslist_base_url)



