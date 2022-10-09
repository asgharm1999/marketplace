from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


def get_etsy_search_results(base_url, search='furniture'):

#   fout = open('Etsy.txt', 'wt',encoding='utf-8')
#   fclean = open('Etsy_clean.txt', 'wt')
    
    search_results = []
    
    url = base_url + search + '&page=1&ref=pagination'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    
    page = soup.find("span", {'class':'wt-display-inline-flex-sm'}).text
    print(page)
    page = 1
#   titles = []
    
    while page < 3:
        url = base_url + search + '&page=' + str(page) + '&ref=pagination'
#       url = f"https://www.etsy.com/search?q=dining+table+and+chairs&ref=auto-1&as_prefix=dining+table+and+chairs&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
#       fout.write(str(soup))
        for item in soup.select('.wt-grid__item-xs-6'): 
            try: 
                print('-------------------------')
                #print(item)
                title = item.select('h3')[0].get_text().strip()
                print(title)
#               fclean.write('title')
                price = item.select('.currency-value')[0].get_text().strip()
                print(price)
#               fclean.write(price)
                rating = item.find("input", {'name': "rating"}).attrs['value']
                print(rating)
#               fclean.write(rating)
                link = item.find('a', {'data-palette-listing-image href'})
#               link = item.find("a", {'class': "listing-link wt-display-inline-block bbc3092379125a8bb"}).attrs['href']
                if(link is None):
                    link = 'Missing'
                print(link)
                search_results.append([link, title, price, rating])
            except: 
                #raise e 
                #b=0  
                print("Failed to Add New Data")
        page = page+1
        
#   fout.close()
#   fclean.close()
    
    columns = ('Post URL', 'Post Title', 'Price', 'Rating')
    df = pd.DataFrame(search_results, columns=columns)
    
    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f'Etsy Results ({timestamp}).csv', index=False)
    
    return df

if __name__ == '__main__':
    etsy_base_url = "https://www.etsy.com/search?q="
    search = 'dining table and chairs'
    data = get_etsy_search_results(etsy_base_url)
    print(data)




