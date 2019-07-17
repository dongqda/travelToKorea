from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [

    path('', views.main, name="main"),

    path('', views.base),
    path('detail/', views.detailpage),

    ]