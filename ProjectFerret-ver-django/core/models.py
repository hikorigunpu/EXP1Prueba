from django.db import models

# Create your models here.

class tecnica(models.Model):
  idtecnica = models.IntegerField(primary_key = True, verbose_name = 'Id de tecnica')
  nombretecnica = models.CharField(max_length = 50, verbose_name = 'Nombre del tecnica')

  def __str__(self):
    return self.nombretecnica

# Modelo para obra
class obra(models.Model):
  idobra = models.IntegerField(primary_key = True, verbose_name = 'Id de obra')
  autor = models.CharField(max_length = 6, verbose_name = 'autor')
  nombre = models.CharField(max_length = 20, verbose_name = 'nombre obra')
  descripcion = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'descripcion obra')
  nombretecnica = models.ForeignKey(tecnica, on_delete = models.CASCADE)
  precio = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'precio de la obra')
  imagen = models.CharField (max_length = 100, null = True, blank = True, verbose_name = 'imagen de la obra')

  def __str__(self):
    return self.idobra

class user(models.Model):
  username = models.CharField(primary_key = True,max_length = 20, verbose_name = 'nombre de user')
  password = models.CharField(max_length = 10, verbose_name = 'contraseña de user')

  def __str__(self):
    return self.username

    
