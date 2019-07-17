from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('detail/', views.detailpage),
    ]