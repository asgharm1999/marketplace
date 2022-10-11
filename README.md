# Furniture Marketplace
-----------------------------------------------

##### Authors:
##### Muhammad Asghar masghar@andrew.cmu.edu 
##### Edvin Handoko ehandoko@andrew.cmu.edu 
##### Sahithya Senthilkumar sahithys@andrew.cmu.edu 
##### Saba Zaheer szaheer@andrew.cmu.edu
<br/>

We provided scrapped data from the following websites AptDeco, Craigslist, RealSimple, Etsy, and YellowPages with recommendations based on location, price, and size. You can also provide a zipcode to get quotes on shipping costs via UHaul. 
<br/>

Users can view both new and second hand furniture and compare. Links will be provided if you chose to purchase. 
<br/>

Pre-scraped CSV results are provided. You will be prompted if you want to use that or compile new data. 
<br/>

## HOW TO RUN: 
<br/>

You will have to pip install the following packages. `folium`, `geopy`, `apify`, `apify-client`.

Download or clone the marketplace repo. In terminal or command line, navigate to the root directory of marketplace folder.
<br/>

Simply run `python3 __main__.py`.
<br/>

Everything is interfaced via the command line with simple prompts. Afterwards, you will be prompted to enter in an API token for RealSimple. To generate an API token please sign up at https://console.apify.com/actors/moJRLRc85AitArpNN#/console and paste it into the prompt. 
<br/>

You can now enter a product you are interested in purchasing (e.g. couches, tables, chairs, etc.) and results will be displayed. 