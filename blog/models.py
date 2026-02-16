from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha = models.DateField()
    def __str__(self):
        return self.titulo