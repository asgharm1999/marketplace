import pandas as pd
import numpy as np
import pip
import csv
import glob
import aptdeco_scraper as aptd
import uhaul_scraper as uhaul
import craiglist_scraper as craigl
import etsy_scraper as etsy
import yellowpages_scraper as yellow

# Required for RealSimple
package = apify
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', '--user', package])
# get_ipython().system('pip install apify')


craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"

print("It is recommended you use your terminal in fullscreen to view all the results.")
product_interest = input("What furniture would you like to browse?")


with open('Users.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',')
     for row in reader:
          if username == row[2]: # if the username shall be on column 3 (-> index 2)
              print "is in file"

              import glob

write_header = True
output_csv = 'new york.csv'     # assume this is not already used

with open(output_csv, 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)

    for csv_filename in glob.glob('*.csv'):
        if csv_filename != output_csv:
            with open(csv_filename) as f_input:
                csv_input = csv.reader(f_input)
                header = next(csv_input)

                if write_header:
                    csv_output.writerow(header)
                    write_header = False

                for row in csv_input:
                    if "new york" in row[1].lower():
                        csv_output.writerow(row)




print("We found this: " + craigslist)


craigl.get_craigslist_search_results(craigslist_base_url)



