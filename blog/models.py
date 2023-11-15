from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    título = models.CharField(max_length=255)
    conteúdo = models.TextField()
    data_de_postagem = models.DateTimeField()

class Comment(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_da_postagem = models.DateTimeField()
    texto = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-data_da_postagem']

class Category(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    post = models.ManyToManyField(Post)