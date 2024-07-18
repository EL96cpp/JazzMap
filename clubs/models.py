from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="Название")
    country = models.CharField(max_length=255, null=False, verbose_name="Страна")
    city = models.CharField(max_length=255, null=False, verbose_name="Город")
    address = models.CharField(max_length=255, null=False, verbose_name="Адрес")
    image = models.ImageField(null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"