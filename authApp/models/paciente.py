from django.db import models
from .personal_salud import personalSalud
from .usuario import Usuario

class Paciente(models.Model):
    idpaciente = models.AutoField(primary_key=True)
    idusuario =models.ForeignKey(Usuario,related_name='paciente',on_delete=models.CASCADE)
    ciudad = models.CharField("Ciudad", max_length=45)
    fecha_nac = models.CharField("Fecha nacimiento", max_length=45)
    direccion = models.CharField("Direccion", max_length=10)
    idpersonal_salud= models.ForeignKey(personalSalud, related_name='paciente', default=0, on_delete=models.CASCADE)
