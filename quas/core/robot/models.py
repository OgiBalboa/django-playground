from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from core.modules import global_parameters
from core.models import Brand, Controller
from multiselectfield import MultiSelectField

CATEGORY_CHOICES = global_parameters.CATEGORY_CHOICES

LABEL_CHOICES = global_parameters.LABEL_CHOICES

ROBOT_APPLICATIONS = global_parameters.ROBOT_APPLICATIONS

AXIS_MOVEMENT = global_parameters.AXIS_MOVEMENT

MOUNTING = global_parameters.MOUNTING

DATASHEET = global_parameters.DATASHEET


class Axis(models.Model):
    name = models.CharField(default="Axis Info", max_length=50)
    axis1_speed = models.IntegerField(default=1)  # degree/s
    axis1_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    axis2_speed = models.IntegerField(default=1)  # degree/s
    axis2_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    axis3_speed = models.IntegerField(default=1)  # degree/s
    axis3_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    axis4_speed = models.IntegerField(default=1)  # degree/s
    axis4_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    axis5_speed = models.IntegerField(default=1)  # degree/s
    axis5_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    axis6_speed = models.IntegerField(default=1)  # degree/s
    axis6_movement = models.CharField(choices=AXIS_MOVEMENT, max_length=50)

    def __str__(self):
        return self.name


class Robot(models.Model):
    # -------------------GENERAL INFOS---------------------------
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    # application = models.CharField(choices=ROBOT_APPLICATIONS, max_length=4)
    application = MultiSelectField(choices=ROBOT_APPLICATIONS, max_length=250, blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField()
    slogan = models.CharField(max_length=100, null=True, blank=True)
    # --------------------RATINGS--------------------------
    performance_rating = models.IntegerField(default=1)
    customer_rating = models.IntegerField(default=1)
    # speed = models.IntegerField(default =1)
    # power = models.IntegerField(default =1)
    # accuracy = models.IntegerField(default =1)

    # -------------------FINANCIAL INFOS-------------------------
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    # ----------------------DATASHEET----------------------------
    working_range_image = models.ImageField(upload_to='robots/working_range_images/')

    number_of_axes = models.IntegerField(default=6)
    payload = models.IntegerField(default=1)  # kg
    reach = models.FloatField(default=1)  # metre
    repeatability = models.FloatField(default=1)  # mm
    picking_cycle = models.FloatField(default=1)  # sec 300x25x25 with 1kg payload
    mounting = MultiSelectField(choices=MOUNTING, max_length=30)
    weight = models.IntegerField(default=1)  # kg

    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)

    axis = models.ForeignKey(Axis, null=True, blank=True,
                                      on_delete=models.PROTECT, unique=True)

    def __str__(self):
        return self.title

    def get_brand_url(self):
        return reverse("core:brand", kwargs={
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

    def get_datasheet(self):
        datasheet = {}
        for data_key in DATASHEET:
            datasheet.update({
                data_key: getattr(self, data_key)
            })
        return datasheet
