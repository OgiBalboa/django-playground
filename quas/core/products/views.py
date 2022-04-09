import random
import string
import json

from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from rest_framework.views import APIView
from rest_framework import viewsets
from core.products.models import Product, Attribute
from core.products.serializers import ProductSerializer, AttributeSerializer

from core.products.utils import findrobot_query as frq


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('productimage_set',
                                                'attribute_set')
    serializer_class = ProductSerializer


class AttributeView(viewsets.ModelViewSet):
    queryset = Attribute.objects.select_related('conf')
    serializer_class = AttributeSerializer


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


class RobotCompareView(APIView):
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


class ProductDetailView(DetailView):
    model = Product
    template_name = "products.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_hidden is False:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return render(request, "404.html", "")