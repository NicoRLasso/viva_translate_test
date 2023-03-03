from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ParticipantsConfig(AppConfig):
    name = 'viva_translate.participants'
    verbose_name = _("Participants")
    
    def ready(self):
        try:
            import viva_translate.participants.views  # noqa F401
        except ImportError:
            pass
