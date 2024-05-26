from django.contrib import admin
from .models import Delivery, Item
from dj_static import Cling

class DeliverAdmin(admin.ModelAdmin):
    list_display=('receivers_name', 'tracking_id')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_name','receiver', 'quantity', 'weight','shipping_cost' )
# Register your models here.

admin.site.register(Delivery, DeliverAdmin)
admin.site.register(Item, ItemAdmin)