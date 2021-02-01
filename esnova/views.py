from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
from serviciosapp.models import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import smtplib
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def gastos_solicitante(request):
    return render(request, 'Gastos_Solicitante.html')

def dependencia(request):
    return render(request, 'dependencias.html')
def datos_personas_dependo(request):
    return render(request, 'datos_personas_dependo.html')

def datos_solicitante(request):
    return render(request, 'datos_solicitante.html')

def medios_estudiar(request):
    return render(request, 'medios_estudiar.html')

def datos_responsable(request):
    return render(request, 'datos_responsable.html')

def ingreso_familiar(request):
    return render(request, 'ingreso_familiar.html')

def iniciar(request):
    matricula=request.POST['matricula']
    contrasenia=request.POST['contrasenia']

    usuarios = Usuario.objects.all()
    for user in usuarios:
        if user.matricula == matricula and user.contrasenia == contrasenia:
            u = user
            context = {
                'usuario':u
            }
            return render(request, 'datos_solicitante.html', context)
    return HttpResponseRedirect('/login')

def registrar(request):
    m=request.POST['matricula']
    e=request.POST['email']
    c=request.POST['contrasenia']
    u = Usuario(matricula = m, email = e, contrasenia = c)
    u.save()
    return HttpResponseRedirect('/')

def recuperar_contrasenia(request):
    return render(request, 'recuperar_contrasenia.html')

def enviar_recuperacion(request):
    matricula=request.POST['matricula']
    usuarios = Usuario.objects.all()
    for user in usuarios:
        if user.matricula == matricula:
            to = user.email
            gmail_user = 'estudio.socioeconomico.nova@gmail.com'
            gmail_pwd = 'NovaUniversitas2021'
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Recuperación de contraseña de cuenta para estudio socioeconomico NovaUniversitas \n'
            print(header)
            msg = header + '\nHola Hace unos minutos recibimos una solicitud sobre que has olvidado la contraseña de tu cuenta de estudio socioeconomico NovaUniversitas, si tú no realizaste esta petición haz caso omiso a este correo. \n\nLa contraseña de tu cuenta es: '+user.contrasenia+'\n\n'
            #gmail_user.encode("utf-8", errors="ignore")
            #to.encode("utf-8", errors="ignore")
            #msg.encode("utf-8", errors="ignore")
            #unicodedata(gmail_user)

            #gmail_user.as_string()

            smtpserver.sendmail(gmail_user, to, msg)
            print('done!')
            smtpserver.close()
            #asunto = "Recuperación cuenta NovaUniversitas"
            #mensaje = "Su contraseña es:"+u.contrasenia
            #send_mail(asunto, mensaje, 'estudio.socioeconomico.nova@gmail.com', [u.email], fail_silently=False)
            return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')
