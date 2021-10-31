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
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.kroger.com/savings/cl/coupons/')
source = driver.page_source
print(source)