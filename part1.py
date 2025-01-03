import requests
from bs4 import BeautifulSoup
# Очистка
# url = "https://"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# rows = soup.find_all("tr")
# data = []
# for row in rows:
#     cols = row.find_all("td")
#     cleaned_cols = [col.text.strip() for col in cols]
#     data.append(cleaned_cols)
#
# print(data)

# Преобразование

# data = [
#
#     ['100', '200', '300'],
#     ['400', '500', '600']
#
# ]
# nums = []
# for row in data:
#     for text in row:
#         number = int(text)
#         nums.append(number)
#
# print(nums)

# Фильтрация
list = []
data = [
    [400, 500, 600],
    [110, 120, 130],
    [140, 500, 600]

 ]
for row in data:
    for item in row:
        if item > 190:
            list.append(item)

print(list)