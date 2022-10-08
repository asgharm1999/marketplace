#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


fout = open('Yellowpages.txt', 'wt',encoding='utf-8')
fclean = open('Yellowpages.txt', 'wt')
search_results = []


# In[48]:


page = 1
titles = []
while page < 6:
    url = f"https://www.yellowpages.com/search?search_terms=Furniture&geo_location_terms=Pittsburgh%2C+PA&page={page}"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html')
    fout.write(str(soup))
    mydivs=soup.find_all("div", {"class": "result"})
    for item in mydivs: 
        try: 
            print('-------------------------')
            name=(item.find("a", {'class':'business-name'}).attrs['href'])
            phone=(item.find("div", {'class':'phones phone primary'}).get_text().strip())
            street_Address=(item.find("div", {'class':'street-address'}).get_text().strip())
            Locality= (item.find("div", {'class':'locality'}).get_text().strip())
            Business_years=(item.find("div", {'class':'years-in-business'}).get_text().strip())
            print(item.find("a", {'class':'business-name'}).attrs['href'])
            print(item.find("div", {'class':'phones phone primary'}).get_text().strip())
            print(item.find("div", {'class':'street-address'}).get_text().strip())
            print(item.find("div", {'class':'locality'}).get_text().strip())
            print(item.find("div", {'class':'years-in-business'}).get_text().strip())
            fclean.write(name)
            fclean.write(phone)
            fclean.write(street_Address)
            fclean.write(Locality)
            fclean.write(Business_years)
        except Exception as e: 
                #raise e 
                b=0
        search_results.append([name,phone, street_Address,Locality,Business_years])
    page = page+1
    

columns = ('Name', 'Phone', 'Street_Address','Locality','Business_years')
df = pd.DataFrame(search_results, columns=columns)


# In[ ]:




