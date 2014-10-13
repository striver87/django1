from django.db import models

class Length(models.Model):
    country = models.CharField(max_length=3)
    length = models.IntegerField()