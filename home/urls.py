from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from django.conf.urls import include
from .views import *


urlpatterns = [
    path('', cache_page(60*60)(HomePageView.as_view()), name='home'),
    path('next_quote/', get_next_quote, name='next_quote'),
    path('previous_quote/', get_previous_quote, name='previous_quote'),
]