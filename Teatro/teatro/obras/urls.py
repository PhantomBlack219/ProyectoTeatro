from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obras/', views.obras, name='obras'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    path('blog/', views.blog, name='blog'),
    path('bloghome/', views.bloghome, name='bh'),
    path('blog1/', views.blog1, name='b1')
]