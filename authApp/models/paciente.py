from django.db import models
from .personal_salud import personalSalud

class Paciente(models.Model):
    idpaciente = models.AutoField(primary_key=True)
    ciudad = models.CharField("Nombre", max_length=45)
    fecha_nac = models.CharField("Apellido", max_length=45)
    direccion = models.CharField("Telefono", max_length=10)
    idpersonal_salud= models.ForeignKey(personalSalud, related_name='paciente', default=0, on_delete=models.CASCADE)
