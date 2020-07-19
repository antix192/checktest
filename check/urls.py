from django.urls import path
from . import views

app_name = 'check'
urlpatterns = [
    path('', views.index, name='index'),
    path('viewhtml', views.viewhtml, name='viewhtml'),
    path('saveData', views.saveData, name='saveData'),
    path('getData', views.getData, name='getData'),
    path('sample1', views.sample1, name='sample1'),
]
