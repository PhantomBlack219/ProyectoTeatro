from django.db import models

# Create your models here.

class Obras(models.Model):
    nombre = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=200)
    foto = models.CharField(max_length=200, default="link")
    

    def get_nombre(self):
        return self.nombre
    def get_sinopsis(self):
        return self.sinopsis
    def get_foto(self):
        return self.foto
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.id)

class Personajes(models.Model):
    nombrep = models.CharField(max_length=200)
    Descripción = models.CharField(max_length=500)
    fotoP = models.CharField(max_length=200, default="link")
    obra =  models.ForeignKey(Obras, on_delete=models.CASCADE)

    def get_nombreP(self):
        return self.nombrep
    def get_descripcion(self):
        return self.Descripción
    def get_fotoP(self):
        return self.fotoP

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombrep, self.id)

class Actores(models.Model):
    nombreA = models.CharField(max_length=200)
    apellidoA =  models.CharField(max_length=200)
    DescripciónA = models.CharField(max_length=500)
    fotoA = models.CharField(max_length=200, default="link")

    def get_nombreA(self):
        return self.nombreA
    def get_descripcionA(self):
        return self.DescripciónA
    def get_fotoA(self):
        return self.fotoA

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombreA + ' '+ self.apellidoA, self.id)