import random
import string
import json
import stripe
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.template.response import TemplateResponse

from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm, ApplicationForm
from .models import Robot, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile, Brand, Controller

from .modules import findrobot_query as frq
stripe.api_key = settings.STRIPE_SECRET_KEY


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def products(request):
    context = {
        'items': Robot.objects.all()
    }
    return render(request, "products.html", context)


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class HomeView(ListView):
    model = Robot
    paginate_by = 10
    template_name = "home.html"



class ItemDetailView(DetailView):
    model = Robot
    template_name = "product.html"

class RobotCompareView(View):
    def get (self,*args,**kwargs):
        funcs = self.request.GET.get("function")
        if funcs and funcs == "get_datasheet":
            robot_1 = self.request.GET.get("robot_1")
            robot_2 = self.request.GET.get("robot_2")
            context = {
                "robot_1": Robot.objects.get(slug = robot_1),
                "robot_2": Robot.objects.get(slug = robot_2),
            }
            return render(self.request, "partials/datasheet-table-double.html", context)
        return render(self.request, "robot-compare.html")
    def post (self,*args,**kwargs):
        pass

class FindRobotView(View):
    def get(self,*args,**kwargs):
        if not self.request.GET.get('query') == "true":
            return render(self.request, "findrobot.html")
        else:
            data = json.loads(self.request.GET.get("parameters"))
            return frq.FindRobot(self.request,data).__get__()
    def post(self, *args,**kwargs):
        return HttpResponse(self.request,"POST",status = 200)
