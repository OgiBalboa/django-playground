from django.urls import path

from . import views

urlpatterns = [
    path('game/', views.game, name='game'),
    path('register/',views.register,name = 'register'),
    path('<str:player_name>/',views.detail,name = "detail"),
]
"""" 
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""