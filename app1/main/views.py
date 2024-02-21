from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import  Categories

# Create your views here.
def index(request):
    
    
    context = {
        'title': 'Home - Головна',
        'content': 'Магазин мебели HOME',

    }
    return render(request, 'main/index.html',context=context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page':'Текст про, чому це товар такий важливий !',
    }
    return render(request, 'main/about.html',context=context)

