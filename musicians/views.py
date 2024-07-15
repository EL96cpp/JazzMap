from django.shortcuts import render
from .models import Musician


def musicians(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians/musicians_list.html', {"musicians": musicians})


def show_musician(request, musician_slug):
    musician = Musician.objects.filter(slug=musician_slug)
    print(musician[0].name, musician[0].image.url)
    return render(request, 'musicians/musician.html', {"musician": musician[0]})
