import json

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from flask import Flask
from flask_restful import Api, Resource
import time

app = Flask(__name__)
api = Api(app)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.maximize_window()


@app.route('/')
class ItemList(Resource):
    def get(self):
        return data, 200


class Item(Resource):
    def get(self, item_id):
        return next(item for item in data if item["id"] == item_id), 200


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

data = []
# data['item'] = []

items = soup.find_all(class_="card savings -coupon card-ui-responsive")
id = 0

for item in items:
    promotion = item.find("div", class_="card-title")
    discount = item.find("div", class_="sub-title")
    description = item.find("span", class_="clamp-2")
    expiration = item.find("div", class_="validity text-block-default")
    image = item.find("img")
    url = item.get('href')
    #data['item'].append({
    data.append({
        'id': id,
        'promotion': promotion.text,
        'discount': discount.text,
        'description': description.text,
        'expiration': expiration.text,
        'src': image['src']
    })

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)