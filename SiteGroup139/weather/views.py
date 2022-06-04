import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm



def index(request):
    appid = 'a34c20e9778841c51281a36546340e35'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    key_error = ''
    for city in cities:

        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
            all_cities.append(city_info)
        except KeyError:
            key_error = 'Город не найден!!!'
            City.objects.all().last().delete()

            # for repeat in all_cities:
            #     for repeat_city in City.objects.all():
            #         if repeat['city'] == repeat_city:
            #             City.objects.all().last().delete()
            #             print(repeat['city'])
    # last_city = City.objects.all().last()
    # city = City.objects.get(name=last_city.name)

    context = {
        'all_info': all_cities,
        'form': form,
        'key_error': key_error,
    }

    return render(request, 'weather/index.html', context)
