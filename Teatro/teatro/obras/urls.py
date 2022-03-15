from unicodedata import name
from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obras/', views.listarObras, name='obras'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    path('blog/', views.blog, name='blog'),
    path('bloghome/', views.bloghome, name='bh'),
    path('blog1/', views.blog1, name='b1'),
    path('obras/<id>/', views.detail_view, name='obras_detalle'),
]