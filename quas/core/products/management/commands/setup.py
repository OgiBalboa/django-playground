import os
import json
from core.products.models import (Attribute, AttributeGroup, AttributeConf,
                                  Product, Brand, ProductImage, Application)

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Setup database for project'

    def add_arguments(self, parser):
        options = [opt for opt in dir(Command) if opt.startswith("_create")]
        parser.add_argument('--all', '-a', type=str, nargs='+',
                            help='The current Django project folder name')
        parser.add_argument('--custom', '-c', type=str,
                            help='tell me what to add! options : {}'.format(
                                "\n".join(options)
                            ))
        parser.add_argument('--path', type=str)
        parser.add_argument('--force', type=bool)

    def handle(self, *args, **kwargs):
        self.path = kwargs.get("path")
        self._create_attribute_groups()
        self._create_attribute_confs()
        self._create_brands()
        self._create_products(force_create=kwargs.get('force'))

    def _create_attribute_groups(self):
        attribute_groups = ['physical', 'commercial', 'efficiency']
        for attribute_group in attribute_groups:
            AttributeGroup.objects.update_or_create(slug=attribute_group,
                                                    name=attribute_group.title())

    def _create_attribute_confs(self):
        fp = os.path.join(self.path, "attribute_confs.json")
        with open(fp, "r") as attr_file:
            robot_attributes = json.load(attr_file)['attributes']
            # TODO: base service to create st
            for attr in robot_attributes:
                if AttributeConf.objects.filter(slug=attr.get('slug')).exists():
                    continue
                attr_groups = attr.pop("attribute_groups")
                """
                new_attr_groups = [AttributeGroup.objects.get(slug=attr_group).id
                                   for
                                   attr_group in attr_groups]
                """
                AttributeConf.objects.update_or_create(**attr)

    def _create_brands(self):
        brands = ["ABB", "NACHI"]
        import datetime
        for brand in brands:
            Brand.objects.update_or_create(name=brand, slug=brand.lower(),
                                           year_of_foundation=datetime.date(
                                               1970, 10, 7))

    def _create_products(self, force_create=False):
        fp = os.path.join(self.path, "products.json")
        with open(fp, "r") as attr_file:
            products = json.load(attr_file)['products']
            for product in products:
                qs = Product.objects.filter(slug=product.get('slug'))
                if qs:
                    if force_create:
                        qs.delete()
                    else:
                        continue
                attributes = product.pop("attributes")
                image = product.pop('image')
                wr_image = product.pop('working_range_image')
                brand = Brand.objects.get(
                    name=product.pop('brand')
                )
                product.update({'brand':brand})
                pro = Product.objects.update_or_create(**product)[0]
                ProductImage.objects.update_or_create(product=pro,
                                            is_active=True,
                                            image=image,
                                            type='default')
                ProductImage.objects.update_or_create(product=pro,
                                            is_active=True,
                                            image=wr_image,
                                            type='working_range')
                self._create_product_attributes(pro, attributes)

    def _create_product_attributes(self, product, attributes):
        for attr in attributes:
            conf = AttributeConf.objects.get(slug=attr.get('slug'))
            attr.update({'conf': conf,
                         'name': conf.name})
            Attribute.objects.update_or_create(product=product,
                                               **attr)
