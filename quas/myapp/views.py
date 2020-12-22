from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import os
def hello(request):
   #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   template = loader.get_template('deneme.html')
   return HttpResponse(template.render())