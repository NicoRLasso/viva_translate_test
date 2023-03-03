from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TeamsConfig(AppConfig):
    name = 'viva_translate.teams'
    verbose_name = _("Teams")
    
    def ready(self):
        try:
            import viva_translate.teams.views  # noqa F401
        except ImportError:
            pass
