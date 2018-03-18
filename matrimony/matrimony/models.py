from django.db import models


class MatrimonyApplication(models.Model):
    name = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    origin = models.CharField(max_length=120)
    gothram = models.CharField(max_length=120)
    family_name = models.CharField(max_length=120)
