from datetime import datetime

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.db import connection
from django import forms

from .models import Item
from .forms import ItemForm
# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello world</h1>')


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
    if request.method == 'POST':
        form = ItemForm(request.POST)
        item = form.save(commit=False)
        item.save()
    else:
        form = ItemForm()
    d = {'items': Item.objects.all(), 'form': form}
    return render(request, 'check/sample1.html', d)
