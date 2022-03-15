from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Obras, Actores, Blog
from .forms import EncuestaForm

#vista para listar Actores
def listarActores(request):
    listaA = Actores.objects.all()
    context = {'listaA':listaA}
    template = loader.get_template('Home/index.html')
    return HttpResponse(template.render(context,request))

#vista para listar Blog
def listarBlog(request):
    listaB = Blog.objects.all()
    context = {'listaB':listaB}
    template = loader.get_template('blog/bloghome.html')
    return HttpResponse(template.render(context,request))


def quienessomos(request):
    template = loader.get_template('Quienes_somos/QuienesSomos.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blog(request):
    template = loader.get_template('blog/blogpost.html')
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

#Vista para ver detalles de un blog
def detail_view_blog(request, id):
    context = {}

    context['object'] = Blog.objects.get(id = id)

    return render(request,'blog/blog_detalle.html',context)

def create_Encuesta(request):

    context = {}

    form = EncuestaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('obras')
    
    context['form'] = form
    return render(request,'oteatro/obras_encuesta.html', context)



