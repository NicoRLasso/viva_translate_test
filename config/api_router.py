from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from viva_translate.competitions.views import CompetitionViewSet
from viva_translate.participants.views import ParticipantViewSet
from viva_translate.teams.views import TeamsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("participant", ParticipantViewSet)
router.register("team", TeamsViewSet)
router.register("competition", CompetitionViewSet)


app_name = "api"
urlpatterns = router.urls
