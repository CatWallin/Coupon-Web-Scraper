import json

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
#import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://www.kroger.com/savings/cl/coupons/')
source = driver.page_source

soup = bs4.BeautifulSoup(source, 'html.parser')

print(soup.title)

'''
buttons = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/main/section/div/section/section/section/div/div[2]/div[2]/div[2]/div/div/ul/li[4]/div/div/div/div[2]/div[1]/button')
buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Shop All Items')]")
print(buttons)
for button in buttons:
    button.click()
    source2 = driver.page_source
    soup2 = bs4.BeautifulSoup(source2, 'html.parser')
    link = soup2.find(class_="kds-Link kds-Link--inherit font-500 no-underline flex flex-row items-center")
    if link is not None:
        print(link.get('data-qa'))
    time.sleep(1)
    back = driver.find_element(By.XPATH, "//button[@data-testid='ModalCloseButton']")
    back.click()
    time.sleep(2)
'''

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
    '''
    print(promotion.text)
    print(expiration.text)
    print(image['src'])
    print(url)
    print()
    '''
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
