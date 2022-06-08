import requests
from django.shortcuts import render
from django.conf import settings
from .models import City


def index(request):
    api_token = settings.MY_API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_token

    # Избегаем дубликаты городов с помощью get_or_create.
    if request.method == 'POST':
        city_input = request.POST.get('city_input')
        city_input = city_input.title()
        City.objects.get_or_create(name=city_input)

    cities = City.objects.all()
    all_cities = []
    key_error = ''

    # Получаем(обновляем) информацию по всем имеющимся на отслеживании городам,
    # проверяем правильность ввода названия города..
    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
            }
            all_cities.append(city_info)
        except KeyError:
            key_error = 'Город не найден!!!'
            City.objects.all().last().delete()
    context = {
        'all_info': all_cities,
        'key_error': key_error,
    }

    return render(request, 'weather/index.html', context)
