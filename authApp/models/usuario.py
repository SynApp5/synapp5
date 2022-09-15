from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self,username):
        if not username:
            raise ValueError('Error al ingresar usuario!')
        user=self.model(username=username)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser,PermissionsMixin):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=45)
    apellido = models.CharField("Apellido", max_length=45)
    telefono = models.CharField("Telefono", max_length=10)
    genero = models.CharField("Género", max_length=45)
    perfil = models.CharField("Perfil", max_length=45)

    def save(self,**kwargs):
        super().save(**kwargs)
    
    objects: UsuarioManager()
    USERNAME_FIELD='username'