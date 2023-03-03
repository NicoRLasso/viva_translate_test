from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from viva_translate.teams.models import Teams
from viva_translate.participants.models import Participants
from viva_translate.participants.serializers import ParticipantSerializer

class TeamSerializer(serializers.ModelSerializer):
    country = CountryField()
    members = ParticipantSerializer(many=True, read_only=True)
    class Meta:
        model = Teams
        fields = [
            'id',
            'name',
            'country',
            'members',
            'representative_name'
        ]


class AddMemberTeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    member_id = serializers.IntegerField()

    def validate(self, attrs):
        try:
            _ = Participants.objects.get(pk=attrs['member_id'])
            _ = Teams.objects.get(pk=attrs['team_id'])
            return attrs
        except:
            raise serializers.ValidationError("wrong values")   
    