import requests
import lxml
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.news_base
collection = db.News_collection
newsposts = db.news

url = 'https://gorvesti.ru'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
test = soup.select(".card")
links = soup.find_all('a')

urls = []
dates = []
titles = []
texts = []
video_link = ""
news = ""
news_text = ''
video_link = ''
video_links =[]
for title in links:
    str = title.get('href')
    if (len(str) > 35 and str[0] == "/" and str[1] != "/"):
        urls.append(url + str)
        # print(url + str)

for news in urls:
    response = requests.get(news)
    soup = BeautifulSoup(response.text, 'lxml')
    header = soup.find(class_='article-title-block')
    main = soup.find(class_='item block')
    dates.append(header.find(class_='dt').text)
    titles.append(header.find(class_='title-block').text)
    texts_default = main.find_all('p')
    video_link_prev = main.find(class_="video")
    if video_link_prev is not None:
        video_link = video_link_prev.find('iframe').src
    for text in texts_default:
        news_text += text.text + "\n"
    texts.append(news_text)
    video_link_prev = main.find(class_='video')
    if video_link_prev is not None:
        video_links.append(video_link_prev.find('iframe').get('src'))
        video_link = video_link_prev.find('iframe').get('src')
        # print(video_link_prev)
        # print(video_link)
    else:
        video_links.append('')
        video_link = ''
    post = {
        'link': news,
        'title': header.find(class_='title-block').text,
        'date': header.find(class_='dt').text,
        'content': news_text,
        'videolink': video_link
    }
    if newsposts.find_one({'link':news}) is None:
        newsposts.insert_one(post)
    news_text=''
    # print(news)
    # print(header.find(class_='dt').text)

