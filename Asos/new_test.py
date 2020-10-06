import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import json


class Shoe:

    kind = ''
    link = ''
    size_list = []
    def __init__(self, name, curr_price, discount):
        self.name = name
        # self.full_price = full_price
        self.curr_price = curr_price
        self.discount = discount
        #self.sizes = size_list
        # self.link = link
        # self.type = kind

    def add_all(self, k, l, s_list):
        self.sizes = s_list
        self.link = l
        self.type = k


full_url = 'https://www.asos.com/men/outlet/shoes-trainers/cat/?cid=27437&currentpricerange=0-210&nlid=mw|outlet|shop%20by%20product&refine=brand:'

sizes = {3.5: 2336,
         4: 2340,
         4.5: 2466,
         5: 2339,
         5.5: 2333,
         6: 2332,
         6.5: 2329,
         7: 2325,
         7.5: 2334,
         8: 2337,
         8.5: 2328,
         9: 2331,
         9.5: 1855,
         10: 2323,
         10.5: 2034,
         11: 2324,
         11.5: 1875,
         12: 2326,
         12.5: 1945,
         13: 2310,
         13.5: 2589}

brands = {
    'Adidas': '17,18,16346,15565',
    'Asics': 13688,
    'Cat': 13656,
    'Jordan': 14269,
    'NB': 499,
    'Nike': '2986,15176,13623,15177',
    'Puma': 589,
    'Saucony': 13540,
    'Timberland': 3672,
    'The north face': 3312,
    'Under Armour': 15203,
    'Vans': 765
    # 'Lacoste': 391,
    # 'Levis': 401,
    # 'EA': 3060,
    # 'Fila': 202,
    # 'Fred Perry': 2943,
    # 'Reebok': '2988,16284',
}

types = {
    'Boots': 8585,
    'Flip-flops': 10775,
    'Trainers': 8606
}

inv_types = {
    8585: 'Boots',
    10775: 'Flip-flops',
    8606: 'Trainers'
}

url_for_adidas = full_url + brands['Adidas'] + '&page=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)  # seconds

driver.get(url_for_adidas)
time.sleep(2)
page = driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section').text
arr = page.split('\n')

names = tuple(arr[::3])
# print([int(s) for s in re.findall(r'-\b\d+\b', s)])
info = (arr[1::3], arr[2::3])
# print(info[0][:])
print(arr[1].split(' '))
adidas_trainers = []
for i in range(len(names)):
    # Same 2 lines, but shorter
    # adidas_trainers.append(Shoe(names[i], info[0][i], [int(info[1][i]) for info[1][i] in re.findall(r'\b\d+\b', info[1][i])]))
    adidas_trainers.append(Shoe(names[i], info[0][i], int(re.search(r'\b\d+\b', info[1][i])[0])))
    # shoes.append(Shoe(names[i], info[0][i], info[1][i]))

print(adidas_trainers[0].name)
counter = 0
print(len(adidas_trainers))
for el in adidas_trainers:
    counter += 1
    if counter == 10:
        break
    # print(counter)
    try:
        driver.find_element_by_xpath('//*[contains(text(), \"{}\")]'.format(el.name)).click()
        time.sleep(1)
        # driver.refresh()
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="chrome-footer"]/footer/div[1]/div[1]'))
        WebDriverWait(driver, 5).until(element_present)
        sz = driver.find_element_by_xpath('//*[@id="main-size-select-0"]').text
        arr = sz.split('\n')
        arr2 = []
        for s in arr:
            # if re.match('[0-9]$', el):
            if re.search('EU.[+-]?([0-9]*[.])?[0-9]+$', s, flags=re.IGNORECASE):
                arr2.append(s)

        el.add_all(inv_types[8606], driver.current_url, arr2)
        # el.sizes = arr2
        # el.link = driver.current_url
        # el.kind = inv_types[8606]
        driver.back()
        print(el.__dict__)
    except selenium.common.exceptions.NoSuchElementException:
        # driver.refresh()
        driver.get(url_for_adidas)
        continue
    except selenium.common.exceptions.ElementClickInterceptedException:
        driver.get(url_for_adidas)
        continue


# driver.find_element_by_xpath('//*[contains(text(), \"{}\")]'.format(adidas_trainers[0].name)).click()
for shoe in adidas_trainers:
    print(shoe.__dict__)

# with open('shoes.txt', 'w') as outfile:
#     outfile.write(adidas_trainers[:])
#
# print(name)

b = [a.name for a in adidas_trainers if a.discount == 33]
for a in b:
    print(a.__dict__)
# try:
#     name = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/h1').text
# except selenium.common.exceptions.StaleElementReferenceException:
#     print('Full xpath didn\`t work')
# finally:
#     name = driver.find_element_by_xpath('//*[@id="aside-content"]/div[1]/h1').text



# element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="chrome-footer"]/footer/div[1]/div[1]'))
# WebDriverWait(driver, 5).until(element_present)
# time.sleep(2)
# page = driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section').text
# print(type(page))
# print(page)
# arr = page.split('\n')
driver.quit()
