from __future__ import division
from django.db import models
from model_utils import Choices


class Product(models.Model):
    product_code = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_unit = models.FloatField()
    BASIC_UNIT = Choices(
        (1, 'kg', 'Kilograms'),
        (2, 'ltr', 'Litre'),
        (3, 'cm', 'Centimetre'),
        (4, 'pcs', 'Pieces'),
        (5, 'pax', 'Pax'),
        (6, 'box', 'Box')
    )
    basic_unit = models.PositiveSmallIntegerField(choices=BASIC_UNIT)
    tax_percentage = models.FloatField()
    limited = models.BooleanField(default=False)
    active_for_sale = models.BooleanField(default=True)
    discounted_price = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def final_price(self):
        return self.discounted_price or self.price


class Stock(models.Model):
    product = models.OneToOneField('products.Product')
    in_stock = models.FloatField()
