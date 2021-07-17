import random
import string
import json
import stripe
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from core.products.models import Product

from core.products.utils import findrobot_query as frq


def get_datasheet(request, *args, **kwargs):
    robot = request.GET.get("products")
    context = {
        "products": Product.objects.get(slug=robot)
    }
    return render(request, "partials/datasheet-table-single.html", context)


def get_datasheets(request, *args, **kwargs):
    robot_1 = request.GET.get("robot_1")
    robot_2 = request.GET.get("robot_2")
    context = {
        "robot_1": Product.objects.get(slug=robot_1),
        "robot_2": Product.objects.get(slug=robot_2),
    }
    return render(request, "partials/datasheet-table-double.html", context)


class RobotCompareView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "products-compare.html")

    def post(self, *args, **kwargs):
        pass


class FindRobotView(View):
    def get(self, *args, **kwargs):
        if not self.request.GET.get('query') == "true":
            return render(self.request, "findrobot.html")
        else:
            data = json.loads(self.request.GET.get("parameters"))
            return frq.FindRobot(self.request, data).__get__()

    def post(self, *args, **kwargs):
        return HttpResponse(self.request, "POST", status=200)


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def products(request):
    context = {
        'items': Product.objects.all()
    }
    return render(request, "products.html", context)


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Product
    template_name = "products.html"
