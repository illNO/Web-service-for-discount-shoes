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

    def __init__(self, name, curr_price, discount, shoe_type, size_list, link):
        self.name = name
        self.curr_price = curr_price
        self.discount = discount
        self.shoe_type = shoe_type
        self.sizes = size_list
        self.link = link

    def add_all(self):
        pass


full_url = 'https://www.asos.com/men/outlet/shoes-trainers/cat/?cid=27437' \
           '&currentpricerange=0-210&nlid=mw|outlet|shop%20by%20product&refine=brand:'

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
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)  # seconds

driver.get(url_for_adidas)
time.sleep(2)
page = driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section').text
data_from_page = page.split('\n')

names = tuple(data_from_page[::3])
info = (data_from_page[1::3], data_from_page[2::3])
adidas_trainers = []
for i in range(len(names)):
    if i % 2 == 0:
        try:
            driver.find_element_by_xpath('//*[contains(text(), \"{}\")]'.format(names[i])).click()
            time.sleep(1)
            driver.refresh()
            sz = driver.find_element_by_xpath('//*[@id="main-size-select-0"]').text
            data_from_page = sz.split('\n')
            shoe_sizes = []
            for s in data_from_page:
                if re.search('EU.[+-]?([0-9]*[.])?[0-9]+$', s, flags=re.IGNORECASE):
                    shoe_sizes.append(s)
            adidas_trainers.append(Shoe(name=names[i],
                                        curr_price=info[0][i],
                                        discount=int(re.search(r'\b\d+\b', info[1][i])[0]),
                                        shoe_type=inv_types[8606],
                                        size_list=shoe_sizes,
                                        link=driver.current_url))
            driver.back()
            print(adidas_trainers[counter].__dict__)
        except selenium.common.exceptions.NoSuchElementException:
            # driver.refresh()
            driver.get(url_for_adidas)
            continue
        except selenium.common.exceptions.ElementClickInterceptedException:
            driver.get(url_for_adidas)
            continue
        except selenium.common.exceptions.StaleElementReferenceException:
            driver.get(url_for_adidas)
            continue


driver.quit()
for shoe in adidas_trainers:
    print(shoe.__dict__)


def obj_dict(obj):
    return obj.__dict__


json_string = json.dumps(adidas_trainers, default=obj_dict)

with open('shoes.json', 'w') as outfile:
    json.dump(json_string, outfile)

with open('shoes.txt', 'w') as outfile:
    json.dump(json_string, outfile)

# Same 2 lines, but shorter
# adidas_trainers.append(Shoe(names[i], info[0][i], [int(info[1][i]) for info[1][i]
# in re.findall(r'\b\d+\b', info[1][i])]))
# shoes.append(Shoe(names[i], info[0][i], info[1][i]))


# element_present = EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="chrome-footer"]/footer/div[1]/div[1]'))
# WebDriverWait(driver, 5).until(element_present)


# if re.match('[0-9]$', el):


# b = [a.name for a in adidas_trainers if a.discount == 33]
# for a in b:
#     print(a.__dict__)

# with open('shoes.txt', 'w') as outfile:
#     outfile.write(adidas_trainers[:])
#
# print(name)


# try:
#     name = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/h1').text
# except selenium.common.exceptions.StaleElementReferenceException:
#     print('Full xpath didn\`t work')
# finally:
#     name = driver.find_element_by_xpath('//*[@id="aside-content"]/div[1]/h1').text


# element_present = EC.presence_of_element_located
# ((By.XPATH, '//*[@id="chrome-footer"]/footer/div[1]/div[1]'))
# WebDriverWait(driver, 5).until(element_present)
# time.sleep(2)
# page = driver.find_element_by_xpath('//*[@id="plp"]/div/div/div[2]/div/div[1]/section').text
# print(type(page))
# print(page)
# arr = page.split('\n')
