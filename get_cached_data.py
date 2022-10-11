import csv
import os
from glob import glob
import pathlib
from posixpath import abspath
import pandas as pd
from turtle import numinput
import re


def get_data_aptdeco():    
    files = os.listdir()
    print(files)
    files_list = []
    pat = r'^AptDeco Results'
    for file in files:
        if re.search(pat, file) != None:
            files_list.append(file)
    print(files_list)
    

get_data_aptdeco()

def get_data():
    path = f"{pathlib.Path().resolve()}/SUMMARY.csv"
    fieldnames = ['post_url', 'price', 'location', 'post_title', 'source']

    d = {os.path.splitext(os.path.basename(f))[0] : pd.read_csv(f) for f in glob(path)} 

    print(d)





    # # CRAIGSLIST
    # craigslist_base_url = "https://pittsburgh.craigslist.org/search/fua"
    # craigl.get_craigslist_search_results(craigslist_base_url)

    # # REALSIMPLE & DANIA 
    # realsimple_base_url = "https://www.realsimple.com/home-organizing/decorating"
    # real.get_realsimple_search_results(realsimple_base_url, realsimple_token)

    # # ETSY
    # etsy_base_url = "https://www.etsy.com/search?q=furniture&page={page}&ref=pagination"
    # etsy.get_etsy_search_results(etsy_base_url)

    # # APTDECO
    # aptdeco_base_url = 
    # aptd.get_aptdeco_search_results(aptdeco_base_url)

    # # YELLOWPAGES
    # yellowpages_base_url = 
    # yp.get_yellowpages_search_results(yellowpages_base_url)

    # # UHAUL
    # uhaul_base_url = 
    # uh.get_uhaul_search_results(uhaul_base_url)