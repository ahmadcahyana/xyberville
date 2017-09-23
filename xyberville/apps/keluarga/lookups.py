from __future__ import unicode_literals
from .models import Keluarga
from selectable.base import ModelLookup
from selectable.registry import registry


class KeluargaLookup(ModelLookup):
    model = Keluarga
    search_fields = (
        'nomor_kk__icontains',
    )

    def get_item_value(self, item):
        # Display for currently selected item
        return item.nomor_kk

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s (%s)" % (item.nomor_kk, item.kepala_keluarga)

registry.register(KeluargaLookup)
