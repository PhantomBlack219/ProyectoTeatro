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
