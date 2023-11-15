from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .form import PostForm

# Create your views here.

class list_posts(ListView):
    model = Post
    template_name = 'blog/index.html'

class detail_post(DetailView):
    model = Post
    template_name = 'blog/detail.html'

class create_post(CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['título','data_de_postagem','conteúdo']
    
class update_post(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['título','data_de_postagem','conteúdo']
    success_url = reverse_lazy('blog:index')



class delete_post(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:index')
