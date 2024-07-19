from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Musician, Instrument
from genres.models import Genre


class MusicianListView(ListView):
    template_name = "musicians/musicians_list.html"
    context_object_name = "musicians"
    paginate_by = 8

    def get_queryset(self):
        musicians = Musician.objects.all()
        musicians = musicians.order_by('first_name')

        instrument_filter = self.request.GET.get('instrument-filter', None)
        genre_filter = self.request.GET.get('genre-filter', None)

        if instrument_filter:
            musicians = musicians.filter(instrument__name=instrument_filter)

        if genre_filter:
            musicians = musicians.filter(genre__name=genre_filter)

        return musicians


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["instruments"] = Instrument.objects.all()
        context["genres"] = Genre.objects.all()
        context["instrument_filter"] = self.request.GET.get('instrument-filter')
        context["genre_filter"] = self.request.GET.get('genre-filter') 
        return context



class MusicianView(DetailView):
    slug_url_kwarg = "musician_slug"
    template_name = "musicians/musician.html"

    def get_object(self, queryset=None):
        musician = Musician.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return musician

