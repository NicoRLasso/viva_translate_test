from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

class Participants(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')
    id_number = models.CharField(max_length=50, null=False, default='')
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    birthdate = models.DateField()
    country = CountryField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"