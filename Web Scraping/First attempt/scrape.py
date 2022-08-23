from bs4 import BeautifulSoup
import requests

with open('site.html','r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='article'):
    headline= article.h2.a.text
    print(headline)

    paragraph=article.p.text
    print(paragraph)
    print()