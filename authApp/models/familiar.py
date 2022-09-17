from django.db import models
from .paciente import Paciente
from .usuario import Usuario


class Familiar(models.Model):
    idfamiliar = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario,related_name='familiar',on_delete=models.CASCADE)
    parentesco = models.CharField("Parentesco", max_length=45)
    correo = models.CharField("Correo", max_length=45)
    idpaciente = models.ForeignKey(Paciente, related_name='familiar', default=0, on_delete=models.CASCADE)