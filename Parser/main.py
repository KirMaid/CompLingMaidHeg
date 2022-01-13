import requests
import lxml
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.news_base
collection = db.News_collection
newsposts = db.news

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
y = 0
for i in range(5000):
    urls.clear()
    url_news = 'https://gorvesti.ru/feed/' + "{}".format(i)
    response = requests.get(url_news)
    soup = BeautifulSoup(response.text, 'lxml')
    links_div = soup.find_all('div','itm-title')
    for title in links_div:
        str = title.find('a').get('href')
        urls.append(url + str)
    for news in urls:
        response = requests.get(news)
        soup = BeautifulSoup(response.text, 'lxml')
        header = soup.find(class_='article-title-block')
        main = soup.find(class_='item block')
        texts_default = main.find_all('p')
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
            'date': header.find(class_='dt').text,
            'content': news_text,
            'videolink': video_link
        }
        newsposts.insert_one(post)
        news_text = ''
