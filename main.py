import json

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://www.publix.com/savings/digital-coupons')

time.sleep(1)

while True:
    try:
        button = driver.find_element(By.XPATH, "//*[contains(text(), 'Load More')]")
    except NoSuchElementException:
        break
    button.click()

source = driver.page_source

soup = bs4.BeautifulSoup(source, 'html.parser')

data = {}
data['item'] = []

items = soup.find_all(class_="card savings -coupon card-ui-responsive")
id = 0

for item in items:
    promotion = item.find("div", class_="card-title")
    discount = item.find("div", class_="sub-title")
    description = item.find("span", class_="clamp-2")
    expiration = item.find("div", class_="validity text-block-default")
    image = item.find("img")
    url = item.get('href')
    data['item'].append({
        'id': id,
        'promotion': promotion.text,
        'discount': discount.text,
        'description': description.text,
        'expiration': expiration.text,
        'src': image['src']
    })

driver.close()

with open("coupon_data.json", "w") as outfile:
    json.dump(data, outfile)

app = Flask(__name__)
api = Api(app)


class Coupons(Resource):
    def get(self):
        return data, 200


api.add_resource(Coupons, '/coupons')

if __name__ == '__main__':
    app.run()

