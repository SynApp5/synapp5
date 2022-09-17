from authApp.models.paciente import Paciente
from authApp.models.usuario import Usuario
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['ciudad', 'fecha_nac', 'direccion']