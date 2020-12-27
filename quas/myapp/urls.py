from django.urls import path

from . import views

urlpatterns = [
    path('game/', views.game, name='game'),
    path('register/',views.register,name = 'register'),
    path('<str:player_name>/',views.detail,name = "detail"),
]
