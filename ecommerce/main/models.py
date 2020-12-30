from django.db import models
from django.conf import settings
from django.shortcuts import reverse
CATEGORIES =  (
    ('C1','Category1'),
    ('C2','Category2'),
    ('C3','Category3'),
)

LABELS =  (
    ('L1','danger'),
    ('L2','Label2'),
    ('L3','Label3'),
)
class Item(models.Model):
    '''
    Item model
    :param name: Item Name (Char)
    :param price: Price (Float)
    :param description: Description (String)
    :param category: Category (String)
    :param label: Label (String)
    :param slug: SLUG (String)
    '''
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    discount_price = models.FloatField(blank=0, null=True)
    discount_amount = models.FloatField(blank=0, null=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=800)
    category = models.CharField(choices=CATEGORIES,max_length=3)
    label = models.CharField(choices=LABELS,max_length=3)
    slug = models.SlugField()
    #features = models.JSONField()

    def get_absolute_url(self):
        return reverse("main:product",kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("main:add_to_cart",kwargs={'slug':self.slug})
    def get_remove_from_cart_url(self):
        return reverse("main:remove_from_cart",kwargs={'slug':self.slug})

    def __str__(self): return self.name
class OrderedItem(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self): return self.item.name+ "({})".format(self.quantity)

class Order (models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    order_date = models.DateField()
    def __str__(self): return self.customer.username
