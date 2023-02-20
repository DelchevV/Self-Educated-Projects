from bs4 import BeautifulSoup
import requests
import csv

with open('file.csv', 'w') as wf:
    csv_writer=csv.writer(wf)
    csv_writer.writerow(['CityName','TempNow','TempTomorrow'])
    source = ''
    searched_city = input(f'Въведи търсен от вас град:\n')
    # Достъпни градове Пловдив, Димитровград, София, Калофер, Бургас, Варна

    while searched_city != '':
        if searched_city=="":
            break
        output = ''
        if searched_city == 'Dimitrovgrad':
            source = requests.get('https://dalivali.bg/?location=71')
        elif searched_city == 'Plovdiv':
            source = requests.get('https://dalivali.bg/?location=173')
        elif searched_city == "Sofia":
            source = requests.get('https://dalivali.bg/?location=217')
        elif searched_city == "Kalofer":
            source = requests.get('https://dalivali.bg/?location=280')
        elif searched_city == 'Burgas':
            source = requests.get('https://dalivali.bg/?location=37')
        elif searched_city == 'Varna':
            source = requests.get('https://dalivali.bg/?location=41')
        elif source == "":
            print("Невалиден град!")
            exit()

        source.encoding = 'utf-8'
        soup = BeautifulSoup(source.text, 'lxml')

        article = soup.find('ul', class_='content-li')
        location = soup.find('div', class_='city-country')

        city = location.h1.text
        country = location.h4.text

        celsium = article.find('div', class_='temperature').find('span', class_='celsium').text
        temperature = article.find('div', class_='temperature').find('span', class_='number').text
        weather_now = article.find('h2', class_='descr').text
        feels_like = article.find('div', class_='gr-num').find('span', class_='num').text
        rain_percent = article.find(id='rain-num').text + '%'
        wind_speed = article.find(id='wind-num').text + 'м/с'
        sun_rise = article.find(id='sunrise-var').text
        sunset = article.find(id='sunset-var').text

        next_day = soup.find(id='content-next-2')
        lower_temp = next_day.find(id='Ntoday1').text
        high = next_day.find(id='tDtoday1').text
        condition = next_day.find('div', class_='weather').h4.text
        output += ('\n-----------------------------------------')
        output += ('\nВ Момента:')
        output += (f'\n{city}, {country} / {temperature}{celsium}')
        output += (f'\n    > {weather_now}')
        output += (f'\n    > Усеща се като {feels_like}{celsium}')
        output += (f'\n    > Валежност {rain_percent}')
        output += (f'\n    > Скорост на вятъра {wind_speed}')
        output += (f'\n    > Изгрев {sun_rise}')
        output += (f'\n    > Залез {sunset}')

        output += ('\nУтре:')
        output += (f'\n{condition} {lower_temp} / {high}')
        output += ('\n-----------------------------------------')
        searched_city = input(f'\nВъведи търсен от вас град:\n')
        csv_writer.writerow([city,temperature+'/'+temperature,lower_temp])
