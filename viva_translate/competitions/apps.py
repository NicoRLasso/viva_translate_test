from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CompetitionsConfig(AppConfig):
    name = "viva_translate.competitions"
    verbose_name = _("Competitions")

    def ready(self):
        try:
            import viva_translate.competitions.views  # noqa F401
        except ImportError:
            pass
