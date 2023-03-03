from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from viva_translate.participants.views import UserViewSet
from viva_translate.teams.views import TeamsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("participant", UserViewSet)
router.register("team", TeamsViewSet)


app_name = "api"
urlpatterns = router.urls
