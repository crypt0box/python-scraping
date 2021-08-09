import json
import time
import requests
import os
import random, string
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup

def randomname(n):
  randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
  return ''.join(randlst)

# 環境変数読み込み
load_dotenv()

INTERVAL = 3

res = requests.get('https://books.rakuten.co.jp/event/book/literature/hontai/')
soup = BeautifulSoup(res.text, 'html.parser')
titles = [n.get_text() for n in soup.select('div.note > a')]
authors = [n.get_text() for n in soup.select('div.note > span')]
links = [n.get('href') for n in soup.select('div.note > a')]

books = dict()
for i in range(len(links)):
  if 'rb' in links[i]:
    try:
      driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER_PATH'])
      time.sleep(INTERVAL)
      driver.get(links[i])
      time.sleep(INTERVAL)
      type_name = driver.find_element_by_xpath("//dl[contains(@class, 'item-imgArea')]/dt/a")
      thumbnail = type_name.get_attribute("href")
      books[randomname(20)] = {
        'title': titles[i],
        'author': authors[i],
        'imageUrl': thumbnail,
        'link': links[i],
        'reward': '本屋大賞'
      }
      driver.quit()
    except: driver.quit()

with open('books.json', mode='wt', encoding='utf-8') as file:
  json.dump(books, file, ensure_ascii=False, indent=2)

print('finish!')