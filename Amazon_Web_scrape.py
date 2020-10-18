#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The code below scrapes mobile review data from amazon.in and then is stored in a csv file which can further be used in sentiment analysis

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from itertools import repeat


# We define a function that takes in URL and mobile name and outputs a pandas data frame
def txt(link, prdt_nmae):
    r = requests.get(link)
    page  = r.content
    
    df = pd.DataFrame()
    
    
    
    product = []

    
    
    soup = bs(page, 'html.parser')
    #print(soup.prettify())
    cous_name = soup.findAll('span', class_='a-profile-name')
    #print(coustomer_name)
    couse_name = []
    
    #loop is created to take in empty list an and the scrapped content and delivers a list of wanted values
    def loop(n, l):
        for i in n:
            l.append(i.get_text())
            
        #print(lis)
    
            
        
    # We take in customer name and an empty list (name from the page scrape) and give it to the function loop
    # We do the same process for all the other veriables that we want to have in our data set
    loop(cous_name, couse_name)
    couse_name.pop(0)
    couse_name.pop(0)
    print(couse_name)
    
    
    
    title = soup.findAll('a', class_= 'review-title-content')
    #print(title)
    cous_title = []
    loop(title, cous_title
         
    # Since the is /n in the review title and the body of the review we need to remove /n from both left and right of the  review
    
    cous_title[:] = [title.lstrip('\n') for title in cous_title]
    cous_title[:] = [title.rstrip('\n') for title in cous_title]
    
    
    review = soup.find_all('i', class_ = 'review-rating')
    rev = []
    
    #for_review(review, rev)
    #print(review)
    loop(review, rev)
    
    rev = [float(title[:3]) for title in rev]
    rev.pop(0)
    rev.pop(0)
    print(rev)
    num = len(rev)
    
    #Review Body
    # since we are not having class we are specifiying  dictionary
    
    review_body = soup.find_all("span",{'data-hook' : 'review-body'})
    rev_body = []
    loop(review_body, rev_body)
    rev_body[:] = [title.lstrip('\n') for title in rev_body]
    rev_body[:] = [title.rstrip('\n') for title in rev_body]
    
    
    
    print(cous_title)
    print(len(cous_title))
    
    product.extend(repeat(prdt_nmae, num))
    print(product)
    
    # we already have our data frame and now we are going to create columns and add the list of datas to it
    
    
    df['Mobile'] = product
    df['Coustomer'] = couse_name
    df['Review_Title'] = cous_title
    df['Review'] = rev_body
    df['Star_Rating_of_5'] = rev
    return df
# These are the URL's used. This code will scrape review data from amazon.in 
# Steps need to be followed:
         # go to amazon.in
         # select a product -> click on review all -> copy the URL 
         # The url must be in this specific order
#url = "https://www.amazon.in/OnePlus-Nord-Gray-128GB-Storage/product-reviews/B08695ZSP6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
#url = "https://www.amazon.in/Apple-iPhone-11-64GB-Green/product-reviews/B07XVKBY68/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

# We are taking user input for how many product data a user wants to scrape:
         # Number of mobile review / any product review the user wants to scrape from amazon.in

n = int(input('number of phone review data to scrape from amazon.in: '))
for i in range(n):
    url = input('enter url to scrape: ')
    ph_nm = input('enter name')
    
    mobile = txt(url, ph_nm)
    
    if i == 0:
        Amazon = mobile
        mobile = 0
    else:
        Amazon = pd.concat([Amazon, mobile], ignore_index = True)
        mobile = 0
   
print(Amazon.head())


# In[2]:


# Check all the values are in the data Frame

Amazon


# In[3]:


# Convert the data Frame into a csv file and store it in the respective path you want

Amazon.to_csv("C:/Users/Rahul K/OneDrive/Desktop/data science/Amazon_Review.csv")


# In[ ]:




