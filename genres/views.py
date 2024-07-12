from django.shortcuts import render
from .models import Genre


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres/genres_list.html', {"genres": genres})
