from authApp.models.signos import Signos
from rest_framework import serializers

class SignosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signos
        fields = ['oximetria', 'frec_cardiaca', 'frec_respiratoria','temperatura','presion_arterial','glicemias','fecha']