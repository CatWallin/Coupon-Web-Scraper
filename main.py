import json

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.maximize_window()

'''
driver.get('https://www.kroger.com/savings/cl/coupons/')
source = driver.page_source

soup = bs4.BeautifulSoup(source, 'html.parser')

print(soup.title)

data = {}
data['item'] = []

items = soup.find_all(class_="AutoGrid-cell flex flex-grow items-stretch")
for item in items:
    promotion = item.find("h3", class_="kds-Heading kds-Heading--s CouponCard-Description mb-0 hover:underline "
                                       "mt-0 font-medium truncate")
    expiration = item.find("span", class_="kds-Text--s CouponExpiration-text CouponExpiration-textDate text-default-700")
    image = item.find("img")
    url = item.get('href')
    data['item'].append({
        'promotion': promotion.text,
        'expiration': expiration.text,
        'src': image['src']
    })
    print(promotion.text)
    print(expiration.text)
    print(image['src'])
    print(url)
    print()
    
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
'''


driver.get('https://www.publix.com/savings/digital-coupons')
source = driver.page_source

soup = bs4.BeautifulSoup(source, 'html.parser')

print(soup.title)

data = {}
data['item'] = []

items = soup.find_all(class_="card savings -coupon card-ui-responsive")
print(items)
for item in items:
    promotion = item.find("div", class_="card-title")
    discount = item.find("div", class_="sub-title")
    description = item.find("span", class_="clamp-2")
    expiration = item.find("div", class_="validity text-block-default")
    image = item.find("img")
    url = item.get('href')
    data['item'].append({
        'promotion': promotion.text,
        'discount': discount.text,
        'description': description.text,
        'expiration': expiration.text,
        'src': image['src']
    })
    print(promotion.text)
    print(discount.text)
    print(description.text)
    print(expiration.text)
    print(image['src'])
    print()

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
