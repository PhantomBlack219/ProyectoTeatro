
from email.policy import default
from django.db import models

# Create your models here.

class Obras(models.Model):
    nombre = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=1000)
    foto = models.CharField(max_length=200, default="link")
    duración= models.CharField(max_length=200)
    genero= models.CharField(max_length=200)
    publico= models.CharField(max_length=200)
    cant_actores=models.IntegerField()
    

    def get_nombre(self):
        return self.nombre
    def get_sinopsis(self):
        return self.sinopsis
    def get_foto(self):
        return self.foto
    def get_duración(self):
        return self.duración
    def get_publico(self):
        return self.publico
    def get_canActores(self):
        return self.cant_actores
    def get_genero(self):
        return self.genero
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.id)

class Personajes(models.Model):
    nombrep = models.CharField(max_length=200)
    Descripción = models.CharField(max_length=11000)
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
    DescripciónA = models.CharField(max_length=1000)
    fotoA = models.CharField(max_length=200, default="link")
    CargoA= models.CharField(max_length=1000)

    def get_nombreA(self):
        return self.nombreA
    def get_apellidoA(self):
        return self.apellidoA
    def get_descripcionA(self):
        return self.DescripciónA
    def get_fotoA(self):
        return self.fotoA
    def get_cargoA(self):
        return self.CargoA

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombreA + ' '+ self.apellidoA, self.id)
    
class Blog(models.Model):
        
    fotoB = models.CharField(max_length=200, default="link")
    tituloP =  models.CharField(max_length=200)
    fechaA = models.CharField(max_length=100)
    nombreAu = models.CharField(max_length=200)
    escritoC = models.CharField(max_Length=10000)
    
    def get_fotoP(self):
        return self.fotoB
    def get_tituloP(self):
        return self.tituloP
    def get_fechaA(self):
        return self.fechaA
    def get_nombreAu(self):
        return self.nombreAu
    def get_escritoC(self):
        return self.escritoC
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.tituloP+ ' '+ self.nombreAu, self.fechaA,self.escritoC)