import pandas as pd
import numpy as np
import os
import pip
import csv
import urllib3
import datetime
import glob
# import aptdeco_scraper as aptd
# import uhaul_scraper as uhaul
# import craiglist_scraper as craigl
# import realsimple_scraper as real
import etsy_scraper as etsy
# import yellowpages_scraper as yellow
# from apify_client import ApifyClient


craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
etsy_base_url = "https://www.etsy.com/search?q=furniture&page={page}&ref=pagination"


etsy.get_etsy_search_results(etsy_base_url)



def import_or_install(package):
    try:
        __import__(package)
    except:
        pip.main(['install', package])       

# Required for RealSimple
packages = ['apify', 'apify-client']
for p in packages:
    import_or_install(p)







# token = "apify_api_Q8Nb6XkPh9ZdZnhkYCZL7BgKB5ZZF531g2xb"
# # Initialize the ApifyClient with your API token
# real.get_realsimple_search_results(realsimple_base_url, token)




# # if not get new data




# product_interest = input("What furniture would you like to browse?")


# with open('Users.csv', 'rt') as f:
#      reader = csv.reader(f, delimiter=',')
#      for row in reader:
#           if username == row[2]: # if the username shall be on column 3 (-> index 2)
#               print "is in file"

#               import glob

# write_header = True
# output_csv = 'new york.csv'     # assume this is not already used

# with open(output_csv, 'w', newline='') as f_output:
#     csv_output = csv.writer(f_output)

#     for csv_filename in glob.glob('*.csv'):
#         if csv_filename != output_csv:
#             with open(csv_filename) as f_input:
#                 csv_input = csv.reader(f_input)
#                 header = next(csv_input)

#                 if write_header:
#                     csv_output.writerow(header)
#                     write_header = False

#                 for row in csv_input:
#                     if "new york" in row[1].lower():
#                         csv_output.writerow(row)




# print("We found this: " + craigslist)


# craigl.get_craigslist_search_results(craigslist_base_url)
