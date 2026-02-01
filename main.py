from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url_google_form = 'https://docs.google.com/forms/d/e/1FAIpQLScaD7aQQqC_-SkGJwkaCTHhHIHTnMS-jge86wIFCfd8MWkmfA/viewform'
url_zilo_clone = "https://appbrewery.github.io/Zillow-Clone/"
input_address_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
input_price_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
input_link_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit_path='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'



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
        address_list.append(link.find('address').getText(strip=True).lstrip())

    return link_list, price_list, address_list

def fill_form(link_list, price_list, address_list):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    

 

    size = len(link_list)
    for i in range(size):
        driver.get(url_google_form)
        time.sleep(3)

        address_input = driver.find_element(By.XPATH, input_address_path)
        price_input = driver.find_element(By.XPATH, input_price_path)
        link_input = driver.find_element(By.XPATH, input_link_path)
        submit = driver.find_element(By.XPATH, submit_path)

        address_input.send_keys(address_list[i])
        price_input.send_keys(price_list[i])
        link_input.send_keys(link_list[i])
        submit.click()
        time.sleep(2) 












link_list, price_list, address_list = search_flats()
fill_form(link_list, price_list, address_list)



time.sleep(1220)

