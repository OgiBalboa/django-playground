from django.urls import path

from . import views

urlpatterns = [
    path('<str:country_name>/<str:date>/<str:case>',views.datas,name = "datas"),
]