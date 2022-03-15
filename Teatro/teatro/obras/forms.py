from attr import fields
from django import forms
from .models import Blog, Obras
from .models import Personajes, Actores

#Crear formulario
class ObrasForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Obras

        #especificar los campos
        fields = [
            'nombre',
            'sinopsis',
            'foto',
            'duración',
            'genero',
            'publico',
            'cantidad actores',
        ]
class PersonajesForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Personajes

        #especificar los campos
        fields = [
            'nombre', 
            'Descripción', 
            'foto', 
            'obra', 
        ]
        
class ActoresForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Actores

        #especificar los campos
        fields = [
            'nombre', 
            'apellido', 
            'Descripción', 
            'foto', 
        ]
        
class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        
        fields = [
            'titulo',
            'fecha',
            'nombre',
            'escrito',
            'foto',
        ]