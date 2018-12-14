
from django.contrib import admin
from django.urls import path, include, re_path
#from rest_framework.authtoken import views as AuthViews
from metrics.utils import custLogin
from pm import views

urlpatterns = [
    path('getLatest', views.index),
    path('addProductivity', views.addProductivity),
    path('search', views.search),
    path('delete', views.delete),
    path('update', views.update)
]

