import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://irkutsk.hh.ru/vacancies/programmist"

driver.get(url)

time.sleep(3)

vacansies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VIUF0yM')

parsed_data = []

for vacancy in vacansies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-16').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-1').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-22').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-16').get_attribute('href')
    except:
        print('произошла ошибка при парсинге')
        continue

    parsed_data.append([title, company, salary, link])


driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
