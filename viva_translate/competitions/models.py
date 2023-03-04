import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from viva_translate.teams.models import Teams

YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]


class Competition(models.Model):
    class Instances(models.TextChoices):
        LOCAL = "LO", _("Local")
        National = "NA", _("National")
        Regional = "RE", _("Regional")
        International = "IN", _("International")

    year = models.IntegerField(
        _("year"), choices=YEAR_CHOICES, default=datetime.date.today().year
    )
    instance = models.CharField(
        max_length=2,
        choices=Instances.choices,
        default=Instances.LOCAL,
    )
    team = models.ForeignKey(
        Teams, related_name="competition_team", on_delete=models.DO_NOTHING
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["year", "instance", "team"], name="unique_record_per_team"
            )
        ]
