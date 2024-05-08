from django.shortcuts import render
from django.urls import path
from . import views


def index(request):
    return render(request, 'index.html')

def tetris(request):
    return render(request, 'Tetris.html')

def culebrita(request):
    return render(request, 'culebrita.html')

urlpatterns = [
    path('', views.index, name='index'),
]


# Create your views here.
