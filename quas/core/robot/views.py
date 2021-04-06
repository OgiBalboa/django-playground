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

from core.models import UserProfile, Brand, Controller
from core.robot.models import Robot, Axis

from core.modules import findrobot_query as frq


def get_datasheet(request, *args, **kwargs):
    robot = request.GET.get("robot")
    context = {
        "robot": Robot.objects.get(slug=robot)
    }
    return render(request, "partials/datasheet-table-single.html", context)


def get_datasheets(request, *args, **kwargs):
    robot_1 = request.GET.get("robot_1")
    robot_2 = request.GET.get("robot_2")
    context = {
        "robot_1": Robot.objects.get(slug=robot_1),
        "robot_2": Robot.objects.get(slug=robot_2),
    }
    return render(request, "partials/datasheet-table-double.html", context)


class RobotCompareView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "robot-compare.html")

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
