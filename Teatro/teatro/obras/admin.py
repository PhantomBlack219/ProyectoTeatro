from django.contrib import admin

# Register your models here.
from .models import Actores, Obras, Personajes

admin.site.register(Actores)
admin.site.register(Obras)
admin.site.register(Personajes)
