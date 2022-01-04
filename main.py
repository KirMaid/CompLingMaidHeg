import requests
from bs4 import BeautifulSoup


url = 'https://gorvesti.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
test = soup.select(".card")
titles = soup.find_all('a')

urls = []
for title in titles:
    str = title.get('href')
    if(len(str) > 35 and str[0]=="/" and str[1]!="/"):
        urls.append(url[:len(url)-1]+str)

print(urls)
#print(name.text)
#print(soup.prettify())
