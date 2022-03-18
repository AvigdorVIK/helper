from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ['Про нас','Наша допомога','Моя потреба','Увійти']

def home(request):
    return render(request,'helpus/home.html', {'menu': menu, 'title': 'Головна'})


def index(request):
    post = Helpus.objects.all()
    return render(request,'helpus/index.html', {'post': post, 'menu': menu, 'title': 'Про нас'})
