from django.urls import path,include
from . import views
app_name = 'main'
urlpatterns = [
    path("itemlist/",views.item_list,name = 'item-list')
]