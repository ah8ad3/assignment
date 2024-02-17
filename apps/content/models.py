from django.db import models
from django.db.models.functions import Coalesce
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _


class Content(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name=_('Content'),
    )
    rating_count = models.PositiveIntegerField(
        default=0, 
        verbose_name=_('Rating Count'),
    )
    rating_average = models.FloatField(
        default=0, 
        verbose_name=_('Rating Average'),
    )

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')

    def __str__(self):
        return str(model_to_dict(self))

    # recalcuate the ratings for this content
    def update_rate(self):
        from apps.rating.models import Rating

        ratings = Rating.objects.aggregate(
            average_rate=Coalesce(
                models.Avg('rate'), 
                models.Value(0)
            ),
            rating_count=models.Count('rate')
        )
        self.rating_count = ratings['rating_count']
        self.rating_average = ratings['average_rate']
        self.save()

    # add new rate to old one
    def add_rate(self, rate: int):
        self.rating_average = (rate + (self.rating_average * self.rating_count)) / (self.rating_count + 1)
        self.rating_count += 1
        self.save()
