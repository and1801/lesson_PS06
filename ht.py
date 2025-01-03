import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://www.divan.ru/irkutsk/category/svet"

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, 'div.yo41A wcwtp')

parsed_data = []

for light in lights:
    try:
        title = light.find_element(By.CSS_SELECTOR, 'span.name').text
        price = light.find_element(By.CSS_SELECTOR, 'span.price').text
        link = light.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8 qUioe ProductName ActiveProduct').get_attribute('href')
    except:
        print('произошла ошибка при парсинге')
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("lights.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)