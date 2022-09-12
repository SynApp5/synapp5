from django.db import models
from .paciente import Paciente
from .personal_salud import personalSalud



class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=45)
    apellido = models.CharField("Apellido", max_length=45)
    telefono = models.CharField("Telefono", max_length=10)
    genero = models.CharField("Género", max_length=45)
    perfil = models.CharField("Perfil", max_length=45)
    idpaciente = models.ForeignKey(Paciente, related_name='usuario', on_delete=models.CASCADE)
    idpersonal_salud = models.ForeignKey(personalSalud, related_name='usuario', on_delete=models.CASCADE)
    