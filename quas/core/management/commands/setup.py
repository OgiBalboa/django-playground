import os
from core.products.models import (Attribute, AttributeGroup,
                                  Product, Brand, Controller, Axis)
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Setup database for project'

    def add_arguments(self, parser):
        options = [opt for opt in dir(Command) if opt.startswith("_create")]
        parser.add_argument('all', type=str, nargs='+', flag='-a',
                            help='The current Django project folder name')
        parser.add_argument('custom', type=str, flag='-c',
                            help='tell me what to add! options : {}'.format(
                                "\n".join(options)
                            ))

    def handle(self, *args, **kwargs):
        self._create_attribute_groups()
        self._create_attributes()
        self._create_brands()

    def _create_attribute_groups(self):
        return

    def _create_attributes(self):
        # TODO: base service to create st
        #Attribute.objects.create()
        print("aha")

    def _create_brands(self):
        return
