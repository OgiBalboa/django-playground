from django.db import models
from core.models import BaseModel
from django.shortcuts import reverse
from django.utils.module_loading import import_string
from core.products.utils import global_parameters
from multiselectfield import MultiSelectField
from core.products.utils.global_parameters import (
    LABEL_CHOICES, PRODUCT_TYPES, DATA_TYPES, IMAGE_TYPES)


class Application(BaseModel):

    def __str__(self):
        return self.name


class AttributeGroup(BaseModel):

    def __str__(self):
        return self.name


class AttributeConf(BaseModel):
    description = models.CharField(max_length=500, blank=True,
                                   null=True)
    is_direct_proportion = models.BooleanField()
    coefficient_mapping = models.JSONField(default=dict, null=True, blank=True)
    attribute_groups = models.ManyToManyField('AttributeGroup')
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=250,
                                    blank=True, null=True)
    data_type = models.CharField(choices=DATA_TYPES, max_length=50)

    def __str__(self):
        return self.name

class Attribute(BaseModel):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    value = models.JSONField(default=dict)
    conf = models.ForeignKey('products.AttributeConf', on_delete=models.CASCADE)
    value_calculator = models.ForeignKey('calculators.ValueCalculator',
                                         null=True, on_delete=models.CASCADE,
                                         blank=True)

    def get_value(self):
        if self.value_calculator:
            return self.value_calculator.calculate()
        if self.conf.data_type not in ['dict', 'list']:
            return self.value.get('default_value')
        return self.value

    def __str__(self):
        return "{} - {}".format(self.product.name,self.name)


# Add customer rating table, image table
class Product(BaseModel):
    main_slug = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=10)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slogan = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    price = models.DecimalField(max_digits=9, decimal_places=2,
                                null=True, blank=True)

    def __str__(self):
        return self.name

    def get_brand_url(self):
        return reverse("core:brand", kwargs={
            'slug': self.brand
        })

    def get_sales_url(self):
        return

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_attributes(self):
        return Attribute.objects.filter(product_id=self.pk)

    def get_attributes_by_attribute_group(self, attribute_group):
        # duzelt
        return Attribute.objects.filter(product_id=self.pk,
                                        conf__attrubte_groups=attribute_group)

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
    """
    Brand info, name, country, date, point, etc...
    """
    # country =
    year_of_foundation = models.DateField()

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='robots/images')
    type = models.CharField(choices=IMAGE_TYPES, max_length=250)
    is_active = models.BooleanField()

    def __str__(self):
        return "{} - {}_{}".format(self.product.name, self.type, self.slug)
