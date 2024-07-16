from django.db import models
from genres.models import Genre


class Instrument(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name="Инструмент")

    class Meta:
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"

    def __str__(self):
        return self.name


class Musician(models.Model):
    first_name = models.CharField(max_length=255, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=255, null=False, verbose_name="Фамилия")
    image = models.ImageField(null=True, verbose_name="Фото")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    instrument = models.ForeignKey(to=Instrument, on_delete=models.PROTECT, null=False, verbose_name="Инструмент")
    genre = models.ManyToManyField(to=Genre, verbose_name="Жанр")
    biography = models.TextField(null=False, verbose_name="Биография")

    class Meta:
        verbose_name = "Музыкант"
        verbose_name_plural = "Музыканты"

    def __str__(self):
        return self.first_name + " " + self.last_name
