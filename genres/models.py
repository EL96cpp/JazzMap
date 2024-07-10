from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name="Название")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
