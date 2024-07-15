from django.shortcuts import render
from .models import Genre


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres/genres_list.html', {"genres": genres})


def show_genre(request, genre_slug):
    genre = Genre.objects.filter(slug=genre_slug)
    print(genre[0].name, genre[0].image.url)
    return render(request, 'genres/genre.html', {"genre": genre[0]})