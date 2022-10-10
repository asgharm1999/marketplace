def furniture(df):
    print('FURNITURES'.center(50, '-'))
    furniture = input("What furniture would you like to browse?")
    #show list of furniture based on the keyword
    #show visualizations/provide options to various visualizations
    link()
    is_movers = input("Do you want to find nearest movers? (y/n)")
    if is_movers == 'y':
        movers()
    
def shops(np):
    print('NEAREST SHOPS'.center(50, '-'))
    zipcode = input("Enter Zipcode: ")
    #show list of shops in the particular zipcode
    
def movers(np):
    print('NEAREST MOVERS'.center(50, '-'))
    zipcode = input('Enter Zipcode: ')
    #show list of shops in the particular zipcode
    
def articles(np):
    print('ARTICLES'.center(50, '-'))
    #show list of articles
        
def link():
    product_link = "Would you like the link to purchase?"

def price():
    product_price = "Price"