from django.db import models
from core.models import BaseModel
from django.shortcuts import reverse
from core.products.utils import global_parameters
from multiselectfield import MultiSelectField

CATEGORY_CHOICES = global_parameters.CATEGORY_CHOICES
LABEL_CHOICES = global_parameters.LABEL_CHOICES
ROBOT_APPLICATIONS = global_parameters.ROBOT_APPLICATIONS
PRODUCT_TYPES = global_parameters.PRODUCT_TYPES
AXIS_MOVEMENT = global_parameters.AXIS_MOVEMENT
AXIS_NUMBER = global_parameters.AXIS_NUMBER
MOUNTING = global_parameters.MOUNTING
DATASHEET = global_parameters.DATASHEET


# TODO: convert titles to name


class AttributeGroup(BaseModel):
    slug = models.CharField(max_length=250)
    name = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    slug = models.CharField(max_length=250)
    name = models.CharField(max_length=350, null=True, blank=True)
    attribute_group = models.ManyToManyField('AttributeGroup')  # groupSS
    product_types = MultiSelectField(choices=PRODUCT_TYPES, max_length=250,
                                     blank=True, null=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    # -------------------GENERAL INFOS---------------------------
    attributes = models.JSONField(default=dict)
    attributes_detailed = models.JSONField(default=dict)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    application = MultiSelectField(choices=ROBOT_APPLICATIONS, max_length=250,
                                   blank=True, null=True)
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=10)
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
    working_range_image = models.ImageField(
        upload_to='robots/working_range_images/')

    number_of_axes = models.IntegerField(default=6)
    payload = models.IntegerField(default=1)  # kg
    reach = models.FloatField(default=1)  # metre
    repeatability = models.FloatField(default=1)  # mm
    picking_cycle = models.FloatField(
        default=1)  # sec 300x25x25 with 1kg payload
    mounting = MultiSelectField(choices=MOUNTING, max_length=30)
    weight = models.IntegerField(default=1)  # kg

    controller = models.ForeignKey('Controller', on_delete=models.CASCADE)

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

    def get_attributes_by_attribute_group(self, attribute_group):
        return

    def get_grouped_attributes(self):
        return

    def calculate_performance_rating(self):
        return

    def calculate_customer_rating(self):
        return

    def calculate_power_rating(self):
        return

    def calculate_speed_rating(self):
        return

    def custom_calculation(self, *args, **kwargs):
        return

    def get_datasheet(self):
        datasheet = {}
        for attribute_group, attributes in global_parameters.ATTRIBUTE_GROUPS.items():
            datasheet[attribute_group] = {}
            for attribute in attributes:
                if attribute == "axis":
                    for i in range(1, self.number_of_axes + 1):
                        datasheet[attribute_group].update({
                            "Axis" + str(i): "Speed : " + str(getattr(self.axis,
                                                                      "axis" + str(
                                                                          i) + "_speed")) + \
                                             "  Movement : " + getattr(
                                self.axis, "axis" + str(i) + "_movement")
                        })
                else:
                    datasheet[attribute_group].update({
                        attribute.replace("_", " ").title(): getattr(self,
                                                                     attribute)
                    })
        datasheet.pop("Information")
        return datasheet


class Brand(BaseModel):
    title = models.CharField(max_length=100)
    '''
    Brand info, name, country, date, point, etc...
    '''

    def __str__(self):
        return self.title


class Controller(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    # ----------------DATASHEET------------------

    def __str__(self):
        return self.title


class RobotClass(BaseModel):
    """
    Classify robots in order to rate them by their production purpose
    """
    title = models.CharField(max_length=50)
    attributes = models.JSONField()
    attributes_detailed = models.JSONField()

    def __str__(self):
        return self.title
