from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Genre


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres/genres_list.html', {"genres": genres})


class GenreView(DetailView):
    slug_url_kwarg = "genre_slug"
    template_name = "genres/genre.html"

    def get_object(self, queryset=None):
        genre = Genre.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return genre
