import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

base_url = "https://www.uhaul.com/Locations/Pittsburgh-PA/Results/"

html = urlopen(base_url)
bsyc = BeautifulSoup(html.read(), "lxml")
fout = open('uhaul_html.txt', 'wt', encoding='utf-8')
fout.write(str(bsyc))
fout.close()

page = requests.get(base_url)
#print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
store_results = soup.find_all('li', {'class': 'divider'})

for store in store_results:
    print(store.prettify())
    
store_info = []

for store in store_results:
    name = store.find('h3', {'class': 'collapse-half medium-uncollapse'}).text
    if(store.find('small', {'class': 'text-semibold'})) != None:
        name = name[3:-55]
    else:
        name = name[3:-3]
    url = store.h3.a['href']
    location = store.find('p', {'class': 'collapse'}).text
    location = location[23:-23]
    contact = store.find('ul', {'class': 'no-bullet collapse'}).find('a').text
    contact = contact[30:-26]
    open_hours = store.find('p', {'class': 'text-callout text-semibold text-lg'}).text
    open_hours = open_hours[10:-6]
    
    store_info.append([url, name, location, contact, open_hours])

columns = ('Store URL', 'Name', 'Location', 'Contact No', 'Operating Hours')
df = pd.DataFrame(store_info, columns=columns)

timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
df.to_csv(f'Uhaul Results ({timestamp}).csv', index=False)    

for info in store_info:
    print(info)