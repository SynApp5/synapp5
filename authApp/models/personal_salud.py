from django.db import models
#from .usuario import Usuario

class personalSalud(models.Model):
    idpersonal_salud = models.AutoField(primary_key=True)
    especialidad = models.CharField("Especialidad", max_length=45)
    registro = models.CharField("Registro Médico", max_length=45)
    rol = models.CharField("Rol", max_length=45)
    #idusuario = models.ForeignKey(Usuario, related_name='personalSalud', on_delete=models.CASCADE)
    