import driver as driver
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import re
import time


URL = 'https://www.asos.com/men/outlet/shoes-trainers/cat/?cid=27437&nlid=mw%7Coutlet%7Cshop%20by%20product&page=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)  # seconds

driver.get(URL)

s = 'Nike Running x Cody Hudson Epic React Phantom trainers in white'


inputElement = driver.find_element_by_xpath('//*[@id="chrome-search"]')
inputElement.send_keys(s)
inputElement.submit()
driver.refresh()

try:
    name = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/h1').text
except selenium.common.exceptions.StaleElementReferenceException:
    print('Full xpath didn\`t work')
finally:
    name = driver.find_element_by_xpath('//*[@id="aside-content"]/div[1]/h1').text

# try:
#     price = driver.find_element_by_xpath('//*[@id="product-price"]/div/span/span[4]/span[1]').text
# except selenium.common.exceptions.NoSuchElementException:
#     print('Full xpath didn\`t work')
# finally:
#     driver.refresh()


price = driver.find_element_by_xpath('//*[@id="product-price"]/div/span/span[4]/span[1]').text
sizes = driver.find_element_by_xpath('//*[@id="main-size-select-0"]').text
arr = sizes.split('\n')
arr2 = []
print(price)
for el in arr:
    # if re.match('[0-9]$', el):
    if re.search('EU.[+-]?([0-9]*[.])?[0-9]+$', el, flags=re.IGNORECASE):
        arr2.append(el)

print(
    '####################################################################################################################')
for el in arr2:
    print(el)

print(driver.current_url)
driver.quit()
