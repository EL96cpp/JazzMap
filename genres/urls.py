from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'genres'

urlpatterns = [
    path('', GenresListView.as_view(), name='genres_list'),
    path('<slug:genre_slug>/', GenreView.as_view(), name='show_genre'),
]