import requests
from bs4 import BeautifulSoup


url = 'https://gorvesti.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
test = soup.select(".card")
links = soup.find_all('a')

urls = []
dates = []
titles = []
texts = []
video_links = []
news = ""
for title in links:
    str = title.get('href')
    if(len(str) > 35 and str[0]=="/" and str[1]!="/"):
        urls.append(url[:len(url)-1]+str)
        print(url[:len(url)-1]+str)

for news in urls:
    response = requests.get(news)
    soup = BeautifulSoup(response.text, 'lxml')
    header = soup.find(class_='article-title-block')
    main = soup.find(class_='item block')
    dates.append(header.find(class_='dt').text)
    titles.append(header.find(class_='title-block').text)
    texts_default = main.find_all('p')
    for text in texts_default:
        news += text.text+"\n"
    texts.append(news)
    print(news)
    print(header.find(class_='dt').text)


#dt = soup.find('.dt').get('href')
#print(dt)

#print(name.text)
#print(soup.prettify())
