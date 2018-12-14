
from django.contrib import admin
from django.urls import path, include, re_path
#from rest_framework.authtoken import views as AuthViews
from metrics.utils import custLogin
from sm import views

urlpatterns = [
    path('getLatest', views.index),
    path('addSprint', views.addSprint),
    path('search', views.search),
    path('delete', views.delete),
    path('update', views.update),
    path('ud/getLatest', views.ud_index),
    path('ud/addUpDown', views.addUpDown),
    path('ud/search', views.ud_search),
    path('ud/delete', views.ud_delete),
    path('ud/update', views.ud_update),
]

