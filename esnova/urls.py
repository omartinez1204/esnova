from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from esnova.views import *
from django.conf import settings
from django.conf.urls.static import static
#from serviciosapp.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^$',index),
    url(r'^login/$',login),
    url(r'^gastos_solicitante/$',gastos_solicitante),
    url(r'^datos_solicitante/$',datos_solicitante),
    url(r'^medios_estudiar/$',medios_estudiar),
    url(r'^datos_responsable/$',datos_responsable),
    url(r'^ingreso_familiar/$',ingreso_familiar),
    url(r'^gasto_familiar/$',gasto_familiar),
    url(r'^dependencias/$',dependencia),
    url(r'^anexar_documentacion/$',anexar_documentos),
    url(r'^archivos/$',anexar_documentos2),
    url(r'^personas_dependientes/$',datos_personas_dependo),
    url(r'^recuperar_contrasenia/$',recuperar_contrasenia),
    url(r'^informacion_adicional/$',informacion_adicional),
    #url(r'^obtenerDatos_Solicitante/$',obtenerDatos_Solicitante),
    path('serviciosapp/', include('serviciosapp.urls')),
    path('iniciar/>',iniciar, name= "iniciar"),
    path('registrar/>',registrar, name= "registrar"),
    path('enviar_recuperacion/>',enviar_recuperacion, name= "enviar_recuperacion"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
