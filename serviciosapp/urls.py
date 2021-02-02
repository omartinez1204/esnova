from django.contrib import admin
from esnova.views import *
from django.urls import include, path
from django.conf.urls import url
from . import views
app_name = 'serviciosapp'
urlpatterns = [
    url(r'^$',index),
    path('obtenerDatos_Solicitante/>',views.obtenerDatos_Solicitante, name= "obtenerDatos_Solicitante"),
    path('obtenermedios_estudiar/>',views.obtenermedios_estudiar, name= "obtenermedios_estudiar"),
    path('datosdelasPersonasQueDependes/>',views.datosdelasPersonasQueDependes, name= "datosdelasPersonasQueDependes"),
    path('obtenerGastos_Solicitante/>',views.obtenerGastos_Solicitante, name= "obtenerGastos_Solicitante"),
    path('obtenerDatos_Responsable/>',views.obtenerDatos_Responsable, name= "obtenerDatos_Responsable"),
    path('obtenerIngresoFamiliar/>',views.obtenerIngresoFamiliar, name= "obtenerIngresoFamiliar"),
]
