from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
