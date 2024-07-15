from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'clubs'

urlpatterns = [
    path('', clubs, name='clubs_list'),
    path('<slug:club_slug>/', show_club, name='club'),
]