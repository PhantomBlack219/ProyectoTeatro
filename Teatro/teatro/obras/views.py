from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    template = loader.get_template('Home/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def obras(request):
    template = loader.get_template('oteatro/obras.html')
    context = {}
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