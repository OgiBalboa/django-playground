from core.products.models import Product, Brand, Attribute
from core.products.utils import global_parameters
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q, Prefetch

class FindRobot:

    def __init__(self,request, data):
        self.q_kwargs = {}  #queries with keyword arguments
        self.q_args = []     #queries with arguments
        self.request = request
        self.parameter_parser(data)

    def parameter_parser(self,data):
        """
        data = [ hint, [values] ]
        """
        for key, value in data.items():
            #print(data)
            if value['hint'] == "gte":
                self.q_kwargs[key+"__gte"] = value['values'][0] #TODO:(soon) daha anlaşılır ve kesin bir hale getir.
            elif value['hint'] == "brand":
                self.q_kwargs[key] = Brand.objects.get(title=data[key][-1][0])
            elif value['hint'] == "multi":
                for value_ in value['values']:
                    #created Q object ->  key__contains = value (matched with short name) and append to args
                    self.q_args.append(Q(**{key+"__contains": global_parameters.match_parameter_with_short_name(value)}))
            else : self.q_kwargs[key] = value['values'][-1]
        self.result = Query(self.request, self.q_args,self.q_kwargs)

    def __get__(self):
        return self.result


def Query(request, args, kwargs):
    from django.forms.models import model_to_dict

    def _get_robots(qs):
        for k, v in kwargs.items():
            print(kwargs)
            qs = qs.filter(Q(attribute__slug=k.split("__gte")[0]) &
                           Q(attribute__value__default_value__gte=int(v)))
        for arg in args:
            qs = qs.filter(arg)
        return qs
    robots = _get_robots(Product.objects.filter())
    if robots :
        values = robots.values()
        values = []
        for i in range(robots.count()):
            values.append(model_to_dict(robots[i]))
            values[i]["absolute_url"] = robots[i].get_absolute_url()
            values[i]["image_url"] = robots[i].productimage_set.get(type='default').image.url
            values[i]["brand_url"] = robots[i].get_brand_url()
            values[i]["brand_name"] = robots[i].brand.name

        #messages.success(request, "Matching Robot found!!") TODO:(soon)message not shown without reloading page
        #response = serializers.serialize('json', list(robots.values()))
        response = json.dumps(list(values), cls=DjangoJSONEncoder)
        return HttpResponse(response, content_type="application/json")
    else:
        #messages.warning(request, "No products found")
        return HttpResponse("ROBOT DOES NOT EXIST",status=200)


class ProductFilter:

    def __init__(self, request, data):
        self.filters = data
        self.result = self.get_result(**self.parse_query_params(data))

    def parse_query_params(self, parameters):
        for p in parameters:
            pass
        return {
            'q_args': [],
            'q_kwargs': {'name':'x'}
        }

    def get_result(self, q_args, q_kwargs):
        return Product.objects.all().prefetch_related(Prefetch(
            'attribute_set', queryset=Attribute.objects.filter(slug='reach',
                                                            value__default_value__gte=0)),
            Prefetch('attribute_set', queryset=Attribute.objects.filter(slug='payload',
                                                                        value__default_value__gte=0)))
        #return Product.objects.filter(*q_kwargs, **q_kwargs)
