from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    year_released = models.DateField()
    img_url = models.TextField(null=True, blank=True)