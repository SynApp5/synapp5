from django.db import models
from .paciente import Paciente

class Signos(models.Model):
    idsignos = models.AutoField(primary_key=True)
    oximetria = models.IntegerField("Oximetria", default=0)
    frec_cardiaca = models.IntegerField("Frecuencia Cardiaca", default=0)
    frec_respiratoria = models.IntegerField("Frecuencia Respiratoria", default=0)
    temperatura = models.DecimalField("Temperatura", default=0, max_digits=3,decimal_places=1)
    presion_arterial = models.IntegerField("Presión Arterial", default=0)
    glicemias = models.CharField("Glicemias", max_length=45)
    fecha = models.DateTimeField("Glicemias", max_length=45)
    idpaciente = models.ForeignKey(Paciente, related_name='signos', default=0, on_delete=models.CASCADE)
    