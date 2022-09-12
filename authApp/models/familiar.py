from django.db import models
from .usuario import Usuario
from .paciente import Paciente


class Familiar(models.Model):
    idfamiliar = models.AutoField(primary_key=True)
    parentesco = models.CharField("Parentesco", max_length=45)
    correo = models.CharField("Correo", max_length=45)
    idusuario = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    idpaciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)