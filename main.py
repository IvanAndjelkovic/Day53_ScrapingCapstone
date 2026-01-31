from bs4 import BeautifulSoup
import requests
# from selenium import webdrive
# from selenium.webdriver.common.by import By 


url_google_form = 'https://docs.google.com/forms/d/e/1FAIpQLScaD7aQQqC_-SkGJwkaCTHhHIHTnMS-jge86wIFCfd8MWkmfA/viewform'
url_zilo_clone = "https://appbrewery.github.io/Zillow-Clone/"

def search_flats():

    response = requests.get(url_zilo_clone)

    content = response.text
    soup = BeautifulSoup(content,'html.parser')

    link_list=[]
    price_list=[]
    address_list=[]
    for link in soup.find_all('li',class_='ListItem-c11n-8-84-3-StyledListCardWrapper'):
        link_list.append(link.find(name='a').get('href'))
        price_list.append(link.find('span').getText(strip=True).strip('+/mo 1 bd'))
        address_list.append(link.find('address').getText(strip=True))

    return link_list, price_list, address_list

link_list, price_list, address_list = search_flats()
print(link_list)




