from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [

    path('', views.main, name="main"),
    path('detail/', views.detailpage),
    path('map/', views.map, name="map"),
    ]