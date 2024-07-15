from django.contrib import admin
from .models import Instrument, Musician


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "instrument", ]
    search_fields = ["first_name", "last_name", ]
    list_filter = ["instrument", "genre"]
    prepopulated_fields = {"slug": ["first_name", "last_name",]}
