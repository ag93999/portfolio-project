from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=250)