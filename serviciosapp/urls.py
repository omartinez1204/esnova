from django.contrib import admin
from esnova.views import *
from django.urls import include, path
from django.conf.urls import url



urlpatterns = [
    url(r'^$',index),
    path('obtenerDatos_Solicitante/>', views.obtenerDatos_Solicitante, name= "obtenerDatos_Solicitante"),
    path('serviciosapp/',include('serviciosapp.urls')),
]
