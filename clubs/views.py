from django.shortcuts import render
from .models import Club


def clubs(request):
    clubs = Club.objects.all()

    countries = Club.objects.order_by().values_list('country').distinct()
    cities = Club.objects.order_by().values_list('city').distinct()

    print(countries, cities)

    return render(request, 'clubs/clubs_list.html', {"clubs": clubs})

    

