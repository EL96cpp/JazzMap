from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'clubs'

urlpatterns = [
    path('', ClubsListView.as_view(), name='clubs_list'),
]