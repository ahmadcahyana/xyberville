from __future__ import unicode_literals

from selectable.base import ModelLookup
from selectable.registry import registry
from .models import User


class UserLookup(ModelLookup):
    model = User
    search_fields = ('name__icontains',
                     'username__icontains')

    def get_item_value(self, item):
        # Display for currently selected item
        return item.username

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s (%s)" % (item.username, item.name)

registry.register(UserLookup)
