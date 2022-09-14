from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=45)
    apellido = models.CharField("Apellido", max_length=45)
    telefono = models.CharField("Telefono", max_length=10)
    genero = models.CharField("Género", max_length=45)
    perfil = models.CharField("Perfil", max_length=45)