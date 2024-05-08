from django.shortcuts import render
from django.urls import path
from . import views


def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', views.index, name='index'),
]


# Create your views here.
