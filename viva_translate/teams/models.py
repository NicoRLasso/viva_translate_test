from django.db import models
from django_countries.fields import CountryField
from viva_translate.participants.models import Participants
# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length=100, null=False, default='')
    country = CountryField()
    representative_name = models.CharField(max_length=100, null=False, default='')
    members = models.ManyToManyField(Participants,related_name='teams_members',blank=True)

    def __str__(self) -> str:
        return f"{self.name} from {self.country.name}"