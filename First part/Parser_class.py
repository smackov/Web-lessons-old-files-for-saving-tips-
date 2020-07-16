# IMPORT libraries
from bs4 import BeautifulSoup
import urllib.request

# CREATE class Parser
class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)  # download html as a code
        self.raw_html = req.read()  # recording html from code (axBmmd234) to normal text (<html> ... <html\>
        self.html = BeautifulSoup(self.raw_html, 'html.parser')  # reading html as we see html in program window

    def parsing(self):
        news = self.html.find_all('a', class_='border-0')

        for item in news:
            title = item.find('span', class_='fz-16 fw-500 heading').get_text(strip=True)
            desc = item.find('span', class_='name-dop d-block fz-12 mt-1').get_text(strip=True)
            href = item.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            f = open('news.txt', 'w', encoding='utf-8')
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\n'
                        f'Описание: {item["desc"]}\n'
                        f'Ссылка: {item["href"]}\n\n**************\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

# START parsing
file = Parser('https://www.ua-football.com/', 'news.txt')
file.run()
