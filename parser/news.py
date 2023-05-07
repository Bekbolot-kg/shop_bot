import requests
from bs4 import BeautifulSoup as BS

URL = 'https://akipress.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
response = requests.get(URL, headers={'User-Agent': user_agent})

if response.status_code == 200:
    soup = BS(response.text, 'html.parser')
    news = soup.find_all('div', class_='body-stretch')[1]

    news_list = []
    for new in news.find_all_next('a', class_='rubric-news-link'):
        news_dic = {}
        news_dic['new'] = new.text
        news_list.append(news_dic)
