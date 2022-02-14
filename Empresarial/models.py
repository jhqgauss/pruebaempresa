from msilib.schema import Class
from django.db import models

# Create your models here.
class Modelo(models.Model):
    nit=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=70)
    telefono=models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nit,self.nombre, self.direccion, self.telefono)
