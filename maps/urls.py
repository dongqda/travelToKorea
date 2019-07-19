from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [

    path('map/', views.map, name="map"),
    path('', views.main, name='main'),
    path('korea/', views.korea, name='korea'),
    path('detail/', views.detailpage),

    ]