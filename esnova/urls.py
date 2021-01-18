from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from esnova.views import *
urlpatterns = [
    url(r'^$',index),
    path('admin/', admin.site.urls),
]
#Comentario nuevo
