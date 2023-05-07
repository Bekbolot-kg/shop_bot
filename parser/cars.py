import requests
from bs4 import BeautifulSoup as BS



URL = "https://www.mashina.kg/search/all/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
response = requests.get(URL, headers={'User-Agent': user_agent})

if response.status_code == 200:
    soup = BS(response.text, "html.parser")
    car_table = soup.find('div', class_="table-view-list")

    cars = []
    for cr in car_table.find_all('div', class_='list-item'):
        car = {}
        car['brand'] = cr.find(class_='name').text.replace('\n', '').replace(' ', '')
        cars.append(car)

