from django.db import models

# Create your models here.

class Urls(models.Model):
    name = models.CharField(max_length=100, blank=True, null= True)
    long_url = models.URLField(null=False, blank=False)
    short_url = models.CharField(max_length=500, null=False, blank=False, unique=True)
