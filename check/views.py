from datetime import datetime

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.db import connection

from .models import Item
# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello world</h1>')


def viewhtml(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'view message',
    }
    return render(request, 'check/view.html', d)


def saveData(request):
    #    cursor = connection.cursor()
    #    query = 'INSERT INTO "check_item" ("item", "price") VALUES (%s,%s)'
    #    paramList = ['raw', '200']
    #    cursor.execute(query, paramList)

    item = Item(item="new", price="100")
    item.save()
    return HttpResponse('save data')


def getData(request):
    #    items = Item.objects.raw('SELECT * FROM check_item')
    items = Item.objects.all()
    return HttpResponse(item.item + ':' + item.price + '<br>' for item in items)


def sample1(request):
    d = {'items': Item.objects.all()}
    print(d)
    return render(request, 'check/sample1.html', d)
