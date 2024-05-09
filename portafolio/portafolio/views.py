from django.shortcuts import render
from django.urls import path
from . import views
import logging


def index(request):
    return render(request, 'index.html')

def tetris(request):
    return render(request, 'Tetris.html')

def culebrita(request):
    return render(request, 'culebrita.html')

def my_view(request):
    logging.debug('Este es un mensaje de depuración')

urlpatterns = [
    path('', views.index, name='index'),
]


# Create your views here.
