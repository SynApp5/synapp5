from authApp.models.historia import Historia
from rest_framework import serializers
from authApp.models.paciente import Paciente

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['sugerencia', 'diagnostico', 'entorno','fecha','descripcion']