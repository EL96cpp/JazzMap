from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name="Название")
    image = models.ImageField(upload_to=f'genres/images/', null=False, verbose_name="Изображение")
    text = models.TextField(null=False, verbose_name="Статья")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
