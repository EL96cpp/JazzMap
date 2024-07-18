from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .models import Musician, Instrument
from genres.models import Genre


def musicians(request):
    musicians = Musician.objects.all()

    instrument_filter = request.GET.get('instrument-filter', None)
    genre_filter = request.GET.get('genre-filter', None)

    print(musicians[1].genre, musicians[1].first_name, musicians[2].genre, musicians[2].first_name)
    
    if instrument_filter:
        musicians = musicians.filter(instrument__name=instrument_filter)

    if genre_filter:
        musicians = musicians.filter(genre__name=genre_filter)

    paginator = Paginator(musicians, 8)
    musicians_dict = dict()

    page_number = request.GET.get('page')
    current_page = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)

    for musician in current_page:
        if musician.first_name[0] in musicians_dict:
            musicians_dict[musician.first_name[0]].append(musician)
        else:
            musicians_dict[musician.first_name[0]] = [musician,]

    musicians_dict = dict(sorted(musicians_dict.items()))

    genres = Genre.objects.all()
    instruments = Instrument.objects.all()

    context = {
        "instrument_filter": instrument_filter,
        "genre_filter": genre_filter,
        "musicians_dict": musicians_dict, 
        "page_obj": page_obj, 
        "genres": genres, 
        "instruments": instruments
    }

    return render(request, 'musicians/musicians_list.html', context)


class MusicianView(DetailView):
    slug_url_kwarg = "musician_slug"
    template_name = "musicians/musician.html"

    def get_object(self, queryset=None):
        musician = Musician.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return musician

# def show_musician(request, musician_slug):
#     musician = Musician.objects.filter(slug=musician_slug)
#     print(musician[0].image.url)
#     return render(request, 'musicians/musician.html', {"musician": musician[0]})
