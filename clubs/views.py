from django.shortcuts import render
from django.views.generic import ListView
from .models import Club


class ClubsListView(ListView):
    template_name = "clubs/clubs_list.html"
    context_object_name = "clubs"
    paginate_by = 4

    def get_queryset(self):
        clubs = Club.objects.all()

        country_filter = self.request.GET.get('country-filter', None)
        city_filter = self.request.GET.get('city-filter', None)

        if country_filter:
            clubs = clubs.filter(country=country_filter)

        if city_filter:
            clubs = clubs.filter(city=city_filter)

        return clubs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = [country[0] for country in Club.objects.order_by().values_list('country').distinct()]
        context["cities"] = [city[0] for city in Club.objects.order_by().values_list('city').distinct()]
        context["country_filter"] = self.request.GET.get('country-filter')
        context["city_filter"] = self.request.GET.get('city-filter') 
        return context
    
