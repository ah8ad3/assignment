from django.contrib.auth.models import User
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _

from apps.content.models import Content


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        verbose_name=_('Content'),
    )
    rate = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Rate'),
    )

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')

    def __str__(self):
        return str(model_to_dict(self))
