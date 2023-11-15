from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    título = models.CharField(max_length=255)
    conteúdo = models.TextField()
    data_de_postagem = models.DateTimeField()