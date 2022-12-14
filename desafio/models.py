from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_dni = models.IntegerField()
    fecha_de_nacimiento = models.DateField(auto_now_add=False, auto_now=False, null=True)

    def __str__(self):
      return f"{self.nombre}, {self.numero_dni},{self.fecha_de_nacimiento}, {self.id}"

