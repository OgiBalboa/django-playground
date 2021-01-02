from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
# Create your tests here.
from .models import *



class OrderTests(TestCase):

    def test_total_price(self):
        total_price = 1500
        self.assertIs(total_price,1500)

class CustomerTests(TestCase):

    def test_regular_order_steps(self):
        pass
    def test_customer_cancels_order (self):
        pass
    def test_customer_cancels_and_repeats_order(self):
        pass
