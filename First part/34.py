# IMPORT libraries
from bs4 import BeautifulSoup
import urllib.request

# REQUEST to site: 'https://www.ua-football.com/'
req = urllib.request.urlopen('https://www.ua-football.com/')
html = req.read()

# ADD object of class BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('a', class_='border-0')

results = []

# General cycle. Getting general news from site
for item in news:
    title = item.find('span', class_='fz-16 fw-500 heading').get_text(strip=True)
    desc = item.find('span', class_='name-dop d-block fz-12 mt-1').get_text(strip=True)
    href = item.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

# RECORDING news to file: 'news.txt'
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\n'
            f'Описание: {item["desc"]}\n'
            f'Ссылка: {item["href"]}\n\n**************\n')
    i += 1

f.close()
