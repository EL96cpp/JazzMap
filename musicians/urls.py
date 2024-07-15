from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'musicians'

urlpatterns = [
    path('', musicians, name='musicians_list'),
    path('<slug:musician_slug>/', show_musician, name='show_musician'),
]