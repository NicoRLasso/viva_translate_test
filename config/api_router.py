from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from viva_translate.participants.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("participant", UserViewSet)


app_name = "api"
urlpatterns = router.urls
