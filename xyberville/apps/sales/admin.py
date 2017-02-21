from django.contrib import admin

from .models import Sale, Item


class ItemInline(admin.StackedInline):
    model = Item
    fk_name = "sale"


class SaleAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


admin.site.register(Sale, SaleAdmin)
admin.site.register(Item)
