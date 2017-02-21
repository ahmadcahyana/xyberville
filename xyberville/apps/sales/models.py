from __future__ import division
import random

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from model_utils import Choices
from model_utils.fields import AutoCreatedField


class SaleQuerySet(models.query.QuerySet):

    def is_active(self):
        return self.exclude(models.Q(status=Sale.STATUS.completed) |
                            models.Q(status=Sale.STATUS.canceled))


class Sale(models.Model):
    customer = models.ForeignKey('users.User', related_name='bought')
    sales_person = models.ForeignKey('users.User', related_name='sales')
    number = models.CharField(max_length=8, db_index=True)
    STATUS = Choices(
        (1, 'pending', 'Pending'),
        (2, 'paid', 'Paid'),
        (3, 'completed', 'Completed'),
        (4, 'canceled', 'Canceled'),
        (5, 'refunded', 'Refunded')
    )
    status = models.PositiveSmallIntegerField(choices=STATUS)
    notes = models.TextField(blank=True)
    created = AutoCreatedField()
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    amount_to_collect = models.FloatField(blank=True, null=True)
    paid = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    canceled = models.DateTimeField(blank=True, null=True)
    cancellation_note = models.TextField(blank=True)
    refunded = models.DateTimeField(blank=True, null=True)
    refund_notes = models.TextField(blank=True)
    RATING = Choices(
        (1, 'one', '1 - Bad'),
        (2, 'two', '2'),
        (3, 'three', '3 - Average'),
        (4, 'four', '4'),
        (5, 'five', '5 - Best'),
    )
    rating = models.PositiveSmallIntegerField(choices=RATING, blank=True,
                                              null=True)
    objects = models.Manager.from_queryset(SaleQuerySet)()

    def __unicode__(self):
        return 'Invoice %s' % self.number

    @classmethod
    def create(cls, user, items_data, **items):
        sale = cls.objects.create(user=user, **items)

        for item in items_data:
            product, quantity = item['product'], item['quantity']
            price = product.final_price * quantity
            try:
                tax_amount = product.tax_percentage * price / 100
            except ZeroDivisionError:
                tax_amount = 0
            sale.items.create(
                product=product, quantity=quantity, price=price,
                tax_amount=tax_amount
            )

        return sale

    @property
    def original_price(self):
        return self.price + self.discount

    @property
    def absolute_url(self):
        return settings.HOST + reverse(
            'backoffice:sales:detail', args=[self.id]
        )

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = ''.join(
                random.choice('123456789ACFHJKLSTUXZ') for i in range(8)
            )
        booking = super(Sale, self).save(*args, **kwargs)
        return booking


class Item(models.Model):
    sale = models.ForeignKey(Sale, related_name='items')
    quantity = models.PositiveSmallIntegerField()
    price = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('products.Product', related_name='items')
    tax_amount = models.FloatField(blank=True, null=True)
