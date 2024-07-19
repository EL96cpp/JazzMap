from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Genre


class GenresListView(ListView):
    template_name = "genres/genres_list.html"
    context_object_name = "genres"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def genres(request):
#     genres = Genre.objects.all()
#     return render(request, 'genres/genres_list.html', {"genres": genres})


class GenreView(DetailView):
    slug_url_kwarg = "genre_slug"
    template_name = "genres/genre.html"

    def get_object(self, queryset=None):
        genre = Genre.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return genre
