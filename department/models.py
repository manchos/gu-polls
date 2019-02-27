from django.db import models
import logging
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
logging.debug('Debug Message')


class Department(MPTTModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название',
    )
    short_name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Сокращенное название'
    )
    slug_name = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Идентификатор',
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Входит в',
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделение'
