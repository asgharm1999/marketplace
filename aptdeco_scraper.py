import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

base_url = "https://www.aptdeco.com/catalog/furniture?region=Northeast+%28NY%2C+NJ%2C+CT%2C+PA%2C+DE%29"

html = urlopen(base_url)
bsyc = BeautifulSoup(html.read(), "lxml")
fout = open('aptdeco_html.csv', 'wt', encoding='utf-8')
fout.write(str(bsyc))
fout.close()

page = requests.get(base_url)
# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")

# num_results = str(soup.find('div', 'Stats__StyledDiv-vrpu8w-0 fuknnX').text)
# num_results = num_results[:-8]
# num_results = int(num_results)
# print(num_results)

product_results = soup.find_all('div', {'class': 'styles__ProductGridCell-sc-1859r2o-0 bFDJTu'})

for product in product_results:
    print(product.prettify())
    
products_info = []

for product in product_results:
    title = product.find('div', {'class': 'Card__ItemName-rr6223-2 hKSDjR'}).text
    product_url = 'https://www.aptdeco.com' + product.find('a', {'class': 'Card__CardLink-rr6223-1 gfTIJo'})['href']
    new_price = product.find('div', {'class': 'Flex__Container-sc-14qf74e-0 Flex__Row-sc-14qf74e-1 dVjRzf djUejJ'}).text
    separator_new_index = new_price.index('•')-1
    if product.find('s', {'class': 'Card__StrikeThrough-rr6223-3 iwsrff'}) != None:
        new_price_index = new_price.index('$',1)
        new_price = new_price[new_price_index:separator_new_index]
    else:
        separator_new_index = new_price.index('•')-1
        new_price = new_price[:separator_new_index]
#    if product.find('li', {'class': 'Card__OriginalPrice-rr6223-5 kXuMgE'}) != None:
#        retail_price = product.find('li', {'class': 'Card__OriginalPrice-rr6223-5 kXuMgE'}).text
#        separator_retail_index = retail_price.index('|') 
#        retail_price = retail_price[12:separator_retail_index]
#    else:
#        retail_price = None
    
    product_page = requests.get(product_url)
    product_soup = BeautifulSoup(product_page.content, "html.parser")
    location = product_soup.find('p', {'class': 'PDPFooter__FooterText-sc-1ngdbbr-5 PDPFooter__SpacedFooterText-sc-1ngdbbr-6 ddMTKT CcsNI'}).text
    separator_location_index = location.index(':')+2
    location = location[separator_location_index:]
    
    products_info.append([product_url, new_price, location, title])

columns = ('Post URL', 'Price', 'Location', 'Post Title')
df = pd.DataFrame(products_info, columns=columns)

timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
df.to_csv(f'AptDeco Results ({timestamp}).csv', index=False)
    
for info in products_info:
    print(info)

