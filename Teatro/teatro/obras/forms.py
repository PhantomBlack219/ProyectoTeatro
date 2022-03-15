from django import forms
from .models import Blog, Obras
from .models import Personajes, Actores, ActoresPersonajes

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
            'cant_actores',
        ]
class PersonajesForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Personajes

        #especificar los campos
        fields = [
            'nombrep', 
            'Descripción', 
            'fotoP', 
            'obra', 
        ]
        
class ActoresForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Actores

        #especificar los campos
        fields = [
            'nombreA', 
            'apellidoA', 
            'DescripciónA', 
            'fotoA',
            'CargoA', 
        ]

class BlogForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Blog

        #especificar los campos
        fields = [
            'fotoB', 
            'tituloB', 
            'fechaB', 
            'nombreB',
            'escritoB', 
        ]
        
class EncuestaForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = ActoresPersonajes

        #especificar los campos
        fields = [
            'Personaje', 
            'Actor',  
        ]        