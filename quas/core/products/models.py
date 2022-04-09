from django.db import models
from core.models import BaseModel
from django.shortcuts import reverse
from core.products.utils import global_parameters
from core.calculators import Calculators
from core.products.utils.global_parameters import (
    LABEL_CHOICES, PRODUCT_TYPES, DATA_TYPES, IMAGE_TYPES)
from core.utils.error_management import ErrorService


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
    value_calculator = models.CharField(choices=Calculators.get_calculators(),
                                        max_length=250, blank=True, null=True)
    calculated_value = models.DecimalField(max_digits=9, decimal_places=2,
                                           null=True, blank=True)

    def get_value(self):
        if self.value_calculator:
            return getattr(Calculators,
                           self.value_calculator)(**self.value).result

        if self.conf.data_type not in ['dict', 'list']:
            return self.value.get('default_value')
        return [self.value, ""]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.calculated_value = self.get_value()[0]
        super(Attribute, self).save(
            force_insert=force_insert, force_update=force_update, using=using,
            update_fields=update_fields)

    def __str__(self):
        return "{} - {}".format(self.product.name, self.name)


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

    performance_rating = models.IntegerField(null=True, blank=True)
    customer_rating = models.IntegerField(null=True, blank=True)

    @property
    def is_hidden(self):
        return self.extra_fields.get("is_hidden") or False

    def save(self, *args, **kwargs):
        try:
            self.customer_rating = self.calculate_customer_rating()
            self.performance_rating = self.calculate_performance_rating()
        except:
            print("ERROR")
        finally:
            super(Product, self).save()

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

    def get_attributes_by_attribute_group(self, attribute_group):
        # duzelt
        return Attribute.objects.filter(product_id=self.pk,
                                        conf__attrubte_groups=attribute_group)

    def calculate_performance_rating(self):
        return getattr(Calculators, 'general_performance_calculator')(
            product=self).result

    def calculate_customer_rating(self):
        return 86

    def custom_calculation(self, *args, **kwargs):
        return

    def get_datasheet(self):
        return self.attribute_set.all()

    def get_variants(self):
        return Product.objects.filter(main_slug=self.main_slug).exclude(pk=self.pk)

    def __str__(self):
        return self.name


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
