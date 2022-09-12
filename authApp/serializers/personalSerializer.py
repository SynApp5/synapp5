from authApp.models.personal import Personal
from rest_framework import serializers

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['balance', 'lastChangeDate', 'isActive']