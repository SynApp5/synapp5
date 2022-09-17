from authApp.models.personal_salud import personalSalud
from rest_framework import serializers

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = personalSalud
        fields = ['especialidad', 'registro', 'rol']