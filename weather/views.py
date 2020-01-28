import requests
from django.shortcuts import render

def index(request):
    appid = '2a585c8e5ed4d31fc04ad1595d4b3755'
    city='London'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = { 'info': city_info }
    return render(request, 'weather/index.html', context)
