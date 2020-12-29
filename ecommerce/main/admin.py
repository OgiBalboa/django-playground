from django.contrib import admin
from .models import Order,OrderedItem,Item

admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(Item)

