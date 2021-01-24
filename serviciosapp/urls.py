from django.contrib import admin
from esnova.views import *
from django.urls import include, path
from django.conf.urls import url
from . import views
app_name = 'serviciosapp'
urlpatterns = [
    url(r'^$',index),
    path('obtenerDatos_Solicitante/>',views.obtenerDatos_Solicitante, name= "obtenerDatos_Solicitante"),
]
