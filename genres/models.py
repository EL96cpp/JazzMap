from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name="Название")
    image = models.ImageField(upload_to=f'genres/images/', null=False, verbose_name="Изображение")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
