from django.contrib import admin
from .models import Club


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "city"]
    search_fields = ["name", "address"]
    list_filter = ["country", "city"]