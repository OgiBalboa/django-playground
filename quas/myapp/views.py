from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import SaveGame

import os
def game(request):
   #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   player = SaveGame.objects.get(player_name = "newbie")
   args = {
      'player_name': player.player_name,
      'top_score': player.top_score,
   }
   template = loader.get_template('game/deneme.html')
   return HttpResponse(template.render(args,request))

def register(request):
   player = SaveGame.objects.get(player_name = "newbie")
   return HttpResponse(player.player_name)

def detail(request, player_name):
   return HttpResponse("You're looking at question %s." % player_name)


def results(request, question_id):
   response = "You're looking at the results of question %s."
   return HttpResponse(response % question_id)


def vote(request, question_id):
   return HttpResponse("You're voting on question %s." % question_id)