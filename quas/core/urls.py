from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views import (
    ItemDetailView,
    HomeView,
    FindRobotView,
    RobotCompareView
)

app_name = 'core'

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("quas.ico")),
        ),
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('brand/<slug>', HomeView.as_view(), name='brand'),
    path('findrobot/', FindRobotView.as_view(), name='findrobot'),
    path('robotcompare/', RobotCompareView.as_view(), name='robotcompare'),

]
