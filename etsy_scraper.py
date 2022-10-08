#!/usr/bin/env python
# coding: utf-8

# In[228]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[229]:


fout = open('Etsy.txt', 'wt',encoding='utf-8')


# In[230]:


fclean = open('Etsy_clean.txt', 'wt')


# In[271]:


search_results = []
page = 1
titles = []

while page < 3:
    url = f"https://www.etsy.com/search?q=dining+table+and+chairs&ref=auto-1&as_prefix=dining+table+and+chairs&page={page}"
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html')
    fout.write(str(soup))
    for item in soup.select('.wt-grid__item-xs-6'): 
        try: 
            print('-------------------------')
            #print(item)
            title = item.select('h3')[0].get_text().strip()
            print(title)
            fclean.write('title')
            price=item.select('.currency-value')[0].get_text().strip()
            print(price)
            fclean.write(price)
            rating=item.find("input", {'name': "rating"}).attrs['value']
            print(rating)
            fclean.write(rating)
            link = item.find("a", {'class': "listing-link wt-display-inline-block bbc3092379125a8bb"}).attrs['href']
            if(link is None):
                link = 'Missing'
            print(link)
            search_results.append([title, price, rating,link])
        except Exception as e: 
                #raise e 
                b=0  
    page = page+1
    

columns = ('Title', 'Price', 'Rating','Link')
df = pd.DataFrame(search_results, columns=columns)


# In[272]:


df


# In[254]:


df.to_csv('Etsy_clean.csv')


# In[226]:


fout.close()
fclean.close()


# In[ ]:




