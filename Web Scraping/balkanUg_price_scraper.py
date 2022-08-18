from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://balkanyug.bg/bg/vodachi-chekmedje/teleskopichi-vodachi')
source.encoding = 'utf-8'
soup = BeautifulSoup(source.text, 'lxml')

with open("balkanug.csv",'w') as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Product',"Code","Price"])

    for article in soup.find_all('div',class_='products col-md-4 col-sm-6 col-xs-12'):

        name= article.find('div', class_='labels clearfix').a.text
        code=article.find('span',class_='code pull-left').text
        price=article.find('a', class_='price').text
        print(f'{name} {code}  Цена: {price}')
        csv_writer.writerow([name,code,price])
        print()

