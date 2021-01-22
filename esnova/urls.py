from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from esnova.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'^$',index),
    url(r'^Gas_Solicitante/$',gastos_solicitante),
    path('admin/', admin.site.urls),
]
#Comentario nuevo
#Eymar Josue. Nuevo comentario.
#Eymar Josue. Nuevo comentario 2.
#cambio eros
#Hola amigos
