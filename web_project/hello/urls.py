from django.urls import path
from . import views

urlpatterns = [
    path('', views.poo, name='index')

]


