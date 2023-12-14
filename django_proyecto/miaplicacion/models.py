from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    biografia= models.TextField(default="Esta es la biografía del autor") 
    leido= models.BooleanField(default=False)
    
    def __str__(self):
        return 'Nombre: ' + self.nombre + '\n Biografía: ' + self.biografia

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    megusta=models.IntegerField(default=0)
    descripcion=models.TextField(default="")
    autor =Autor(nombre="Desconocido")
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE, default=autor.id)
    tipo=models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Poema(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    descripcion= models.TextField()
    proyecto= models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    megusta= models.IntegerField(default=0)
    guardado=models.BooleanField(default=False)
    leido= models.BooleanField(default=False)
    autor =Autor(nombre="Desconocido")
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE, default=autor.id)


    def __str__(self):
        return 'Título: ' + self.titulo + ' Libro: '+ self.proyecto.nombre

class Capitulo(models.Model):
    numero= models.IntegerField(default=1)
    nombre= models.CharField(max_length=200, default="")
    contenido= models.TextField()
    autor =Autor(nombre="Desconocido")
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE, default=autor.id)
    megusta=models.IntegerField(default=0)
