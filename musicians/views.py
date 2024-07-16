from django.shortcuts import render
from .models import Musician


def musicians(request):
    musicians = Musician.objects.all()
    musicians_dict = dict()

    for musician in musicians:
        if musician.first_name[0] in musicians_dict:
            musicians_dict[musician.first_name[0]].append(musician)
        else:
            musicians_dict[musician.first_name[0]] = [musician,]

    musicians_dict = dict(sorted(musicians_dict.items()))

    return render(request, 'musicians/musicians_list.html', {"musicians_dict": musicians_dict})


def show_musician(request, musician_slug):
    musician = Musician.objects.filter(slug=musician_slug)
    print(musician[0].image.url)
    return render(request, 'musicians/musician.html', {"musician": musician[0]})
