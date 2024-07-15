from django.urls import path, re_path
from django.conf.urls import include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('next_quote/', get_next_quote, name='next_quote'),
    path('previous_quote/', get_previous_quote, name='previous_quote'),
]