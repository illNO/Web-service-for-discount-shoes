from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re
import time


class Shoe:
    def __init__(self, name, price, discount, sizes=[]):
        self.name = name
        self.price = price
        self.discount = discount
        self.sizes = sizes

URL = 'https://www.asos.com/men/outlet/shoes-trainers/cat/?cid=27437&nlid=mw%7Coutlet%7Cshop%20by%20product&page=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)  # seconds

driver.get(URL)

# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="chrome-footer"]/footer/div[1]/div[1]'))
# WebDriverWait(driver, 5).until(element_present)
time.sleep(2)
page = driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section').text

print(type(page))
print(page)
arr = page.split('\n')

names = tuple(arr[::3])
keys = (arr[1::3], arr[2::3])

shoes = []

for i in range(len(names)):
    shoes.append(Shoe(names[i], keys[0][i], keys[1][i]))
for shoe in shoes:
    print(shoe.__dict__)

print(shoes['name': 'adidas Originals ZX Flux trainers in silver'])
# print(len(page))
# print(len(names))
# print(len(keys[0]))
# print(len(keys[1]))
# print(page)
# print(dict)
# 4761
# 5111
driver.quit()
'''inputElement = driver.find_element_by_id("a1")
inputElement.send_keys('1')'''