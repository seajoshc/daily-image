from django.db import models
from django.utils import timezone


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_taken = models.DateField(default=timezone.now)
    labels = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
