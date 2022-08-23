from bs4 import BeautifulSoup
import requests
import csv

source=''
searched_city=input(f'Въведи търсен от вас град:\n')

if searched_city=='Dimitrovgrad':
    source=requests.get('https://dalivali.bg/?location=71')
elif searched_city=='Plovdiv':
    source=requests.get('https://dalivali.bg/?location=173')
elif searched_city=="Sofia":
    source=requests.get('https://dalivali.bg/?location=217')
elif source=="":
    print("Невалиден град!")
    exit()

source.encoding='utf-8'
soup=BeautifulSoup(source.text,'lxml')

article= soup.find('ul', class_='content-li')
location=soup.find('div',class_='city-country')

city=location.h1.text
country=location.h4.text

celsium= article.find('div',class_='temperature').find('span',class_='celsium').text
temperature=article.find('div',class_='temperature').find('span',class_='number').text

next_day=soup.find(id='content-next-2')
lower_temp=next_day.find(id='Ntoday1').text
high=next_day.find(id='tDtoday1').text
condition=next_day.find('div', class_='weather').h4.text
print('-----------------------------------------')
print('В Момента:')
print(f'{city}, {country} / {temperature}{celsium}')


print('\nУтре:')
print(f'{condition} {lower_temp} / {high}')
print('-----------------------------------------')

