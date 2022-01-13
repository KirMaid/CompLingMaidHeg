import datetime

import requests
import lxml
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.news_base
collection = db.News_collection
newsposts = db.news

month = ['Янв', 'Фев', 'Мар', 'Апр', 'Мая', 'Июня', 'Июля', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
now = datetime.datetime.now()
current_day = str(now.day)
current_month = month[int(now.month)-1]
current_date = ''
url = 'https://gorvesti.ru'
urls = []
dates = []
titles = []
texts = []
video_link = ""
news = ""
news_text = ''
video_link = ''
video_links = []
url_news = 'https://gorvesti.ru/feed/1'
response = requests.get(url_news)
soup = BeautifulSoup(response.text, 'lxml')
links_div = soup.find_all('div', 'itm-title')
for title in links_div:
    str = title.find('a').get('href')
    urls.append(url + str)
for news in urls:
    response = requests.get(news)
    soup = BeautifulSoup(response.text, 'lxml')
    header = soup.find(class_='article-title-block')
    main = soup.find(class_='item block')
    texts_default = main.find_all('p')
    current_date = header.find(class_='dt').text
    if len(current_date) < 6:
        current_date = current_day + ' '+current_month + ' '+ current_date
    video_link_prev = main.find(class_="video")
    if video_link_prev is not None:
        video_link = video_link_prev.find('iframe').src
    for text in texts_default:
        news_text += text.text + "\n"
    video_link_prev = main.find(class_='video')
    if video_link_prev is not None:
        video_link = video_link_prev.find('iframe').get('src')
    else:
        video_link = ''
    post = {
        'link': news,
        'title': header.find(class_='title-block').text,
        'date': current_date,
        'content': news_text,
        'videolink': video_link
    }
    if newsposts.find_one({'link': news}) is None:
        newsposts.insert_one(post)
        news_text = ''
