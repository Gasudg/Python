from django.db import models

from django.db import models

class Author(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Category)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

