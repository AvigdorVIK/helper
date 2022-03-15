from django.http import HttpResponse
from django.shortcuts import render

menu = ['Про нас','Наша допомога','Моя потреба','Увійти']

def home(request):
    return render(request ,'helpus/home.html', {'menu': menu, 'title': 'Головна'})


def index(request):
    return render(request ,'helpus/index.html', {'menu': menu, 'title': 'Про нас'})
