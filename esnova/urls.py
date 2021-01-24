from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from esnova.views import *
from serviciosapp.views import *


urlpatterns = [
    url(r'^$',index),
    url(r'^$',index),
    url(r'^login/$',login),
    url(r'^gastos_solicitante/$',gastos_solicitante),
    url(r'^datos_solicitante/$',datos_solicitante),
    url(r'^medios_estudiar/$',medios_estudiar),
    url(r'^datos_responsable/$',datos_responsable),
    #url(r'^obtenerDatos_Solicitante/$',obtenerDatos_Solicitante),
    path('admin/', admin.site.urls),

]
#Comentario nuevo
#Eymar Josue. Nuevo comentario.
#Eymar Josue. Nuevo comentario 2.
#cambio eros
#Hola amigos
