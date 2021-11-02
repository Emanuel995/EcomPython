from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.


class Productos (models.Model):
    nombre = models.CharField(null=True, blank=True, max_length=150)
