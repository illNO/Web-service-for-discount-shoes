import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re

URL = 'https://www.asos.com/adidas-originals/adidas-originals-stan-smith-leather-trainers-in' \
      '-white/prd/12165651?colourwayid=16364817&SearchQuery=&cid=11950'

URL1 = 'https://www.asos.com/adidas/adidas-ultraboost-20-trainers-in-black-boost-blue-violet/' \
       'prd/21071371?CTAref=We+Recommend+Carousel_1&featureref1=we+recommend+pers'

URL3 = 'https://www.asos.com/nike/nike-air-force-1-07-trainers-in-black/prd/14625780?CTAref' \
       '=We+Recommend+Carousel_1&featureref1=we+recommend+pers'

URL4 = ''

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(15)  # seconds

driver.get(URL1)

try:
    name = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/h1').text
except selenium.common.exceptions.StaleElementReferenceException:
    print('Full xpath didnt work')
finally:
    name = driver.find_element_by_xpath('//*[@id="aside-content"]/div[1]/h1').text

price = driver.find_element_by_xpath('//*[@id="product-price"]/div/span/span[4]/span[1]').text
sizes = driver.find_element_by_xpath('//*[@id="main-size-select-0"]').text
print(type(driver.find_element_by_xpath('//*[@id="main-size-select-0"]')))
# //*[@id="plp"]/div/div/div[2]/div/div[1]/section

# print(sizes)
print(name)
print(price)
print(sizes)
arr = sizes.split('\n')
# for el in arr:
#     print(el)
print(
    '####################################################################################################################')
# print(arr)
arr2 = []
# pattern = '^EU[+-]?([0-9]*[.])?[0-9]+$'

for el in arr:
    # if re.match('[0-9]$', el):
    if re.search('EU.[+-]?([0-9]*[.])?[0-9]+$', el, flags=re.IGNORECASE):
        arr2.append(el)

print(
    '####################################################################################################################')
for el in arr2:
    print(el)
driver.quit()

'''
EU 38 - Not available
EU 40
EU 41
EU 42
EU 43
EU 44
EU 45 - Not available
EU 46 - Not available
EU 47.5 - Not available
##################################
EU 38 - Not available
EU 40
EU 41
EU 42.5
EU 44
EU 45 - Not available
EU 46 - Not available
EU 47.5 - Not available

'''
