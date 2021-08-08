import time
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup

# 環境変数読み込み
load_dotenv()

INTERVAL = 3

res = requests.get('https://books.rakuten.co.jp/event/book/literature/hontai/')
soup = BeautifulSoup(res.text, 'html.parser')
detail_urls = [n.get('href') for n in soup.select('div.image > a') if 'rb' in n.get('href')]

for i in range(3):
  driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER_PATH'])
  time.sleep(INTERVAL)
  driver.get(detail_urls[i])
  time.sleep(INTERVAL)
  type_name = driver.find_element_by_xpath("//dl[contains(@class, 'item-imgArea')]/dt/a")
  print(type_name.get_attribute("href"))
  driver.quit()