from core.products.models import Product, Brand
from core.products.utils import global_parameters
from django.http import HttpResponse
import json
from django.db.models import Q

class FindRobot:

    def __init__(self,request, data):
        self.q_kwargs = {}  #queries with keyword arguments
        self.q_args = []     #queries with arguments
        self.request = request
        self.parameter_parser(data)
    def parameter_parser(self,data):
        '''
        data = [ hint, [values] ]
        '''
        for key in data.keys():
            #print(data)
            if data[key][0] == "gte":
                self.q_kwargs[key+"__gte"] = data[key][-1][0] #TODO:(soon) daha anlaşılır ve kesin bir hale getir.
            elif data[key][0] == "brand":
                self.q_kwargs[key] = Brand.objects.get(title=data[key][-1][0])
            elif data[key][0] == "multi":
                for value in data[key][-1]:
                    #created Q object ->  key__contains = value (matched with short name) and append to args
                    self.q_args.append(Q(**{key+"__contains": global_parameters.match_parameter_with_short_name(value)}))
            else : self.q_kwargs[key] = data[key][-1][0]
        self.result = Query(self.request, self.q_args,self.q_kwargs)

    def __get__(self):
        return self.result
def Query(request, args, kwargs):
    robots = Product.objects.filter(*args, **kwargs)
    #robots = Robot.objects.filter(Q(application__contains = "AS" ))
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
        #messages.warning(request, "No products found")
        return HttpResponse("ROBOT DOES NOT EXIST",status=200)
