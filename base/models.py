from django.db import models

# Create your models here.

class Urls(models.Model):
    long_url = models.URLField(null=False, blank=False)
    short_url = models.CharField(max_length=500, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
