from django.db import models
from .personal_salud import personalSalud
from .historia import Historia

class Paciente(models.Model):
    idpaciente = models.AutoField(primary_key=True)
    ciudad = models.CharField("Nombre", max_length=45)
    fecha_nac = models.CharField("Apellido", max_length=45)
    direccion = models.CharField("Telefono", max_length=10)
    idpersonal_salud= models.ForeignKey(personalSalud, related_name='paciente', on_delete=models.CASCADE)
    #idusuario = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    idhistoria = models.ForeignKey(Historia, related_name='paciente',on_delete=models.CASCADE)