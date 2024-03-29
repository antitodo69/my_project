from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Animal(TimeStampedModel):
    name_male = models.CharField(_('Animal male name'), max_length=255, blank=True, null=True)
    name_female = models.CharField(_('Animal female name'), max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name_male}({self.name_female})'
