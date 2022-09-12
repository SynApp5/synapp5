from django.db import models

class Historia(models.Model):
    idhistoria = models.AutoField(primary_key=True)
    sugerencia = models.CharField("Sugerencia", max_length=45)
    diagnostico = models.CharField("Diagnostico", max_length=45)
    entorno = models.CharField("Entorno", max_length=45)
    fecha = models.DateField("Fecha", max_length=45)
    descripcion = models.CharField("Descripcion", max_length=45)
    #idpaciente = models.ForeignKey(Paciente, related_name='historia', on_delete=models.CASCADE)
    