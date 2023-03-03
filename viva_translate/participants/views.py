from viva_translate.participants.models import Participants
from viva_translate.participants.serializers import ParticipantSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class UserViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    """
    A viewset for viewing and editing Participants instances.
    """
    serializer_class = ParticipantSerializer
    queryset = Participants.objects.all()