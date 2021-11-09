from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.


class Producto (models.Model):
    nombre = models.CharField(null=True, blank=True, max_length=150)
    precio = models.DecimalField(max_digits=9, null=True, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to="productos", null=True)

    class Meta:
        db_table="productos"

    def __str__(self):
        return f"[{self.id}] {self.nombre}"