from core.models import Robot
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import json

class FindRobot:

    def __init__(self,request, data):
        self.query = {}
        self.request = request
        self.parameter_parser(data)
    def parameter_parser(self,data):
        for key in data.keys():
            if data[key][0] == "gte":
                self.query[key+"__gte"] = data[key][-1] #TODO:(soon) daha anlaşılır ve kesin bir hale getir.
            else : self.query[key] = data[key][-1]
        self.result = Query(self.request, self.query)

    def __get__(self):
        return self.result
def Query(request, parameters):
    robots = Robot.objects.filter(**parameters)
    if robots :
        values = robots.values()
        for i in range(len(values)):
            values[i]["absolute_url"] = robots[i].get_absolute_url()
            values[i]["image_url"] = robots[i].image.url
            values[i]["brand_url"] = robots[i].get_brand_url()
            values[i]["brand_name"] = robots[i].brand.title
        #messages.success(request, "Matching Robot found!!") TODO:(soon)message not shown without reloading page
        #response = serializers.serialize('json', list(robots.values()))
        response = json.dumps(list(values))
        return HttpResponse(response, content_type="application/json")
    else:
        #messages.warning(request, "No robot found")
        return HttpResponse("ROBOT DOES NOT EXIST",status=200)
