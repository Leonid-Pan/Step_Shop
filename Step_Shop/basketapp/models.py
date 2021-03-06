from django.db import models

from Step_Shop import settings
from mainapp.models import Product


class Basket(models.Model):
    user =models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_detetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзины"
