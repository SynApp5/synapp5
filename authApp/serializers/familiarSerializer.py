from authApp.models.familiar import Familiar
from authApp.models.paciente import Paciente
from authApp.models.usuario import Usuario

from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['parentesco', 'correo']