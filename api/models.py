from django.db import models

# Create your models here.
class BurseData(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True, unique=True)
    api_key = models.CharField(verbose_name='Ключ публичный', max_length=255, blank=True, null=True, unique=True)
    api_secret = models.CharField(verbose_name='Ключ секретный', max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Ключ биржи'
        verbose_name_plural = 'Ключи биржи'

    def __str__(self):
        return self.name
