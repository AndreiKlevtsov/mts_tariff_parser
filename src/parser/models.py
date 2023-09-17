from django.db import models


class Tariff(models.Model):
    """
    Модель тариф.
    """
    name = models.CharField(
        verbose_name='Название тарифа',
        max_length=100,
        unique=True
    )
    description = models.CharField(
        verbose_name='Описание тарифа',
        max_length=255,
        null=True
    )
    features = models.CharField(
        verbose_name='Опции тарифа',
        max_length=255,
        null=True
    )
    benefits = models.CharField(
        verbose_name='Дополнительно к тарифу',
        max_length=255,
        null=True
    )
    main_price = models.CharField(
        verbose_name='Основная цена',
        max_length=255,
        null=True
    )
    sale_price = models.CharField(
        verbose_name='Цена со скидкой',
        max_length=255,
        null=True
    )
    price_annotation = models.CharField(
        verbose_name='Дополнительные условия',
        max_length=255,
        null=True
    )
    badge_text = models.CharField(
        verbose_name='Акционные условия',
        max_length=255,
        null=True
    )


    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        ordering = ["name"]

    def __str__(self):
        return self.name
