from authApp.models.signos import Signos
from rest_framework import serializers

class SignosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signos
        fields = ['balance', 'lastChangeDate', 'isActive']