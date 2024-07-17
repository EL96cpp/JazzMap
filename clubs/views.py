from django.shortcuts import render
from .models import Club


def clubs(request):
    clubs = Club.objects.all()

    countries = [country[0] for country in Club.objects.order_by().values_list('country').distinct()]
    cities = [city[0] for city in Club.objects.order_by().values_list('city').distinct()]

    print(countries, type(cities))

    return render(request, 'clubs/clubs_list.html', {"clubs": clubs, "countries": countries, "cities": cities})

    
