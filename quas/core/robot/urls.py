from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from core.robot.views import FindRobotView, RobotCompareView, get_datasheet, get_datasheets, ItemDetailView, HomeView
app_name = 'core'

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("quas.ico")),
         ),
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('brand/<slug>', HomeView.as_view(), name='brand'),
    path('findrobot/', FindRobotView.as_view(), name='findrobot'),
    path('robotcompare/', RobotCompareView.as_view(), name='robotcompare'),
    path('get_datasheet/', get_datasheet, name='get_datasheet'),
    path('get_datasheets/', get_datasheets, name='get_datasheets'),

]