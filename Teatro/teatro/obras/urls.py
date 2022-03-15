from unicodedata import name
from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('', views.listarActores, name='index'),
    path('obras/', views.listarObras, name='obras'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    path('blog/', views.blog, name='blog'),
    path('bloghome/', views.bloghome, name='bh'),
    path('blog/<id>/', views.detail_view_blog, name='b1'),
    path('obras/<id>/', views.detail_view, name='obras_detalle'),
]



