from rest_framework import serializers
from viva_translate.participants.models import Participants
from django_countries.serializer_fields import CountryField

class UserSerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = Participants
        fields = [
            'id',
            'first_name',
            'last_name',
            'id_number',
            'gender',
            'birthdate',
            'country'
        ]