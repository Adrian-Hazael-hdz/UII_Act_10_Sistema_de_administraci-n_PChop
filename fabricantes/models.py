from django.db import models


# Create your models here.
class Fabricante(models.Model):
  Fabricante_id = models.PositiveIntegerField()
  Nombre = models.CharField(max_length=50)
  Pais = models.CharField(max_length=50)
  sitio_web = models.CharField(max_length=50)
  logo_url = models.CharField(max_length=250)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return f'Fabricante: {self.Nombre} {self.Pais}'