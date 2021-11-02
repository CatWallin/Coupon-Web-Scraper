import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
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
items = soup.find_all(class_="AutoGrid-cell flex flex-grow items-stretch")
for item in items:
    promotion = item.find("h3", class_="kds-Heading kds-Heading--s CouponCard-Description mb-0 hover:underline "
                                       "mt-0 font-medium truncate")
    expiration = item.find("span", class_="kds-Text--s CouponExpiration-text CouponExpiration-textDate text-default-700")
    image = item.find("img")
    url = item.get('href')
    print(promotion.text)
    print(expiration.text)
    print(image['src'])
    print(url)
    print()