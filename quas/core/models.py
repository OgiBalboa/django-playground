from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField
from .modules import global_parameters
from multiselectfield import MultiSelectField

CATEGORY_CHOICES = global_parameters.CATEGORY_CHOICES

LABEL_CHOICES = global_parameters.LABEL_CHOICES

ADDRESS_CHOICES = global_parameters.ADDRESS_CHOICES

ROBOT_APPLICATIONS = global_parameters.ROBOT_APPLICATIONS

AXIS_MOVEMENT = global_parameters.AXIS_MOVEMENT

MOUNTING = global_parameters.MOUNTING
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Brand(models.Model):
    title = models.CharField(max_length=100)
    '''
    Brand infos, name, country, date, point, etc...
    '''
    def __str__(self):
        return self.title
class Controller(models.Model):
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)

    #----------------DATASHEET------------------

    def __str__(self):
        return self.title
class Robot(models.Model):
    # -------------------GENERAL INFOS---------------------------
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    #application = models.CharField(choices=ROBOT_APPLICATIONS, max_length=4)
    application = MultiSelectField(choices=ROBOT_APPLICATIONS, max_length=250,blank=True,null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField()
    slogan = models.CharField(max_length=100,null=True,blank=True)
    #--------------------RATINGS--------------------------
    performance_rating = models.IntegerField(default=1)
    customer_rating = models.IntegerField(default=1)
    #speed = models.IntegerField(default =1)
    #power = models.IntegerField(default =1)
    #accuracy = models.IntegerField(default =1)

    # -------------------FINANCIAL INFOS-------------------------
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    # ----------------------DATASHEET----------------------------
    working_range_image = models.ImageField(upload_to='robots/working_range_images/')

    number_of_axes = models.IntegerField(default=6)
    payload = models.IntegerField(default = 1)# kg
    reach = models.FloatField(default =1) # metre
    repeatability = models.FloatField(default=1)# mm
    picking_cycle = models.FloatField(default=1)# sec 300x25x25 with 1kg payload
    mounting = MultiSelectField (choices=MOUNTING,max_length=30)
    weight = models.IntegerField(default=1) # kg

    axis1_speed = models.IntegerField(default=1)# degree/s
    axis1_movement = models.CharField(choices=AXIS_MOVEMENT,max_length=50)

    axis2_speed = models.IntegerField(default=1)# degree/s
    axis2_movement = models.CharField(choices=AXIS_MOVEMENT,max_length=50)

    axis3_speed = models.IntegerField(default=1)# degree/s
    axis3_movement = models.CharField(choices =AXIS_MOVEMENT,max_length=50)

    axis4_speed = models.IntegerField(default = 1)# degree/s
    axis4_movement = models.CharField(choices =AXIS_MOVEMENT,max_length=50)

    axis5_speed = models.IntegerField(default=1)# degree/s
    axis5_movement = models.CharField(choices=AXIS_MOVEMENT,max_length=50)

    axis6_speed = models.IntegerField(default=1)# degree/s
    axis6_movement = models.CharField(choices=AXIS_MOVEMENT,max_length=50)

    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_brand_url(self):
        return reverse("core:brand", kwargs= {
            'slug': self.brand
        })
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Robot, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
