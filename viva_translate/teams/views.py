from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from viva_translate.participants.models import Participants
from viva_translate.teams.models import Teams
from viva_translate.teams.serializers import AddMemberTeamSerializer, TeamSerializer


class TeamsViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Participants instances.
    """

    serializer_class = TeamSerializer
    queryset = Teams.objects.all()

    @action(
        detail=True,
        methods=["get"],
        url_path=r"add-member/(?P<member_pk>\w+)",
        url_name="add_member",
    )
    def add_member(self, request, pk=None, member_pk=None):
        serializer = AddMemberTeamSerializer(
            data={"team_id": pk, "member_id": member_pk}
        )
        if serializer.is_valid(raise_exception=True):
            team = Teams.objects.get(pk=serializer.validated_data["team_id"])
            if team.members.count() < 3:
                participant = Participants.objects.get(
                    pk=serializer.validated_data["member_id"]
                )
                if team.country == participant.country:
                    team.members.add(participant)
                    team.save()
                    serializer_class = TeamSerializer(team)
                    return Response(
                        data=serializer_class.data, status=status.HTTP_202_ACCEPTED
                    )
                return Response(
                    {"Message": f"All members must be from {team.country.name}"}
                )
            return Response({"Message": "The Team already have 3 participants"})

    @add_member.mapping.delete
    def remove_member(self, request, pk=None, member_pk=None):
        serializer = AddMemberTeamSerializer(
            data={"team_id": pk, "member_id": member_pk}
        )
        if serializer.is_valid(raise_exception=True):
            team = Teams.objects.get(pk=serializer.validated_data["team_id"])
            team.members.remove(
                Participants.objects.get(pk=serializer.validated_data["member_id"])
            )
            serializer_class = TeamSerializer(team)
            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
