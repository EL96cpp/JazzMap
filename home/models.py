from django.db import models


class Quote(models.Model):
    text = models.TextField(max_length=300, null=False, verbose_name="Текст")
    author = models.CharField(max_length=40, null=False, verbose_name="Автор")

