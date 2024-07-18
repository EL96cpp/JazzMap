from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Club


def clubs(request):
    clubs = Club.objects.all()

    countries = [country[0] for country in Club.objects.order_by().values_list('country').distinct()]
    cities = [city[0] for city in Club.objects.order_by().values_list('city').distinct()]

    country_filter = request.GET.get('country-filter', None)
    city_filter = request.GET.get('city-filter', None)

    if country_filter:
        clubs = clubs.filter(country=country_filter)
    if city_filter:
        clubs = clubs.filter(city=city_filter)

    paginator = Paginator(clubs, 4)
    page_number = request.GET.get('page')
    current_page = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)

    context = {
        "clubs": current_page,
        "countries": countries,
        "cities": cities,
        "page_obj": page_obj,
    }

    return render(request, 'clubs/clubs_list.html', context)

    
