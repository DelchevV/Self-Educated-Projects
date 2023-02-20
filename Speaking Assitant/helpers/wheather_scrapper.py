from bs4 import BeautifulSoup
import requests


def make_prediction():
    source = requests.get('https://dalivali.bg/?location=71')
    soup= BeautifulSoup(source.text,'lxml')
    article = soup.find('ul', class_='content-li')

    rain_perc=soup.find('span', class_='rain-num').text
    temperature=article.find('div', class_='temperature').find('span', class_='number').text
    text=f"The weather in your town is {temperature} degrees and there is {rain_perc} percents to rain"
    if int(rain_perc)>50:
        text+=f'\n Please take an umbrella with you!'
    if int(temperature)>25:
        text+=f'\n Today is gonna be a hot one, take a sunscreen'
    return text
