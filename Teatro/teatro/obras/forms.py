from django import forms
from .models import Obras
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