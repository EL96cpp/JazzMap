from django.shortcuts import render
from .models import Club


def clubs(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/clubs_list.html', {"clubs": clubs})


def show_club(request, club_id):
    club = Club.objects.filter(id=club_id)
    return render(request, 'clubs/club.html', {"club": club})
    

