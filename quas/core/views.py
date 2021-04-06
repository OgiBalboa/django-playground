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
from core.models import UserProfile, Brand, Controller
from core.robot.models import Robot, Axis

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

