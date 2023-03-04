from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from viva_translate.participants.models import Participants
from viva_translate.participants.serializers import ParticipantSerializer


class ParticipantViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = ParticipantSerializer
    queryset = Participants.objects.all()
