from django.db import models
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=800)
    #features = models.JSONField()

    def __str__(self): return self.name
class OrderedItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

    def __str__(self): return self.item.name

class Order (models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    order_date = models.DateField()
    def __str__(self): return self.customer.name
