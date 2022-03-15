from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Obras, Actores

#vista para listar Actores
def listarActores(request):
    listaA = Actores.objects.all()
    context = {'listaA':listaA}
    template = loader.get_template('Home/index.html')
    return HttpResponse(template.render(context,request))

def quienessomos(request):
    template = loader.get_template('Quienes_somos/QuienesSomos.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blog(request):
    template = loader.get_template('blog/blogpost')
    context = {}
    return HttpResponse(template.render(context,request))

def bloghome(request):
    template = loader.get_template('blog/bloghome')
    context = {}
    return HttpResponse(template.render(context,request))

def blog1(request):
    template = loader.get_template('blog/blog1')
    context = {}
    return HttpResponse(template.render(context,request))

#vista para listar obras
def listarObras(request):
    lista = Obras.objects.all()
    context = {'lista':lista}
    template = loader.get_template('oteatro/obras.html')
    return HttpResponse(template.render(context,request))


#Vista para ver detalles de una obra
def detail_view(request, id):
    context = {}

    context['object'] = Obras.objects.get(id = id)

    return render(request,'oteatro/obras_detalle.html',context)