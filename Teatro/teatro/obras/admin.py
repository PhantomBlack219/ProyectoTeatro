from django.contrib import admin

# Register your models here.
from .models import Actores, Obras, Personajes, Blog, ActoresPersonajes

admin.site.register(Actores)
admin.site.register(Obras)
admin.site.register(Personajes)
admin.site.register(Blog)
admin.site.register(ActoresPersonajes)
