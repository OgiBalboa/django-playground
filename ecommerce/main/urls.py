from django.urls import path,include
from . import views
app_name = 'main'
urlpatterns = [
    path("",views.HomeView.as_view(), name = 'home-page'),
    path("product/<slug>/",views.ProductPage.as_view(), name = 'product'),
    path('add-to-cart/<slug>',views.add_to_cart,name="add_to_cart"),
    path('remove-from-cart/<slug>',views.remove_from_cart,name="remove_from_cart"),
]