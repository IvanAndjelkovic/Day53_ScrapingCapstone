from bs4 import BeautifulSoup
import requests


url_google_form = 'https://docs.google.com/forms/d/e/1FAIpQLScaD7aQQqC_-SkGJwkaCTHhHIHTnMS-jge86wIFCfd8MWkmfA/viewform'
url_zilo_clone = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(url_zilo_clone)

content = response.text
# with open(response) as file:
#     content=file.read()

soup = BeautifulSoup(content, "html.parser")
# links = soup.findall(name='a', class_='property-card-link')
# for link in soup.find_all( name = 'a', class_='property-card-link'):
#     print(link.get('href'))

# print(soup.find('span').getText())

# for link in soup.find_all(name = 'div' , class_='StyledPropertyCardPhotoWrapper'):
#     # print(link.find(name='a').get('href'))
#     # print(link)
#     print(link)

for link in soup.find_all('li',class_='ListItem-c11n-8-84-3-StyledListCardWrapper'):
    print(link.find(name='a').get('href'))
    print(link.find('span').getText())



