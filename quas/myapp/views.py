from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import SaveGame
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
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
   question = get_object_or_404(Question, pk=question_id)
   try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
      return render(request, 'polls/detail.html', {
         'question': question,
         'error_message': "You didn't select a choice.",
      })
   else:
      selected_choice.votes += 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.

      # reverse redirecst to the function :results in this module
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #Return the last five published questions.
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""