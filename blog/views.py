from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment, Category
from .form import PostForm, CommentForm

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
    success_url = reverse_lazy('blog:index')
    
class update_post(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['título','data_de_postagem','conteúdo']
    success_url = reverse_lazy('blog:index')



class delete_post(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:index')


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_autor = form.cleaned_data['autor']
            comment_texto = form.cleaned_data['texto']
            comment_data_da_postagem = form.cleaned_data['data_da_postagem']
            comment = Comment(autor=comment_autor,
                            texto=comment_texto,
                            data_da_postagem=comment_data_da_postagem,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('blog:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'blog/comment.html', context)

class category_detail(DetailView):
    model = Category
    template_name = 'blog/category.html'

class category_list(ListView):
    model = Category
    template_name = 'blog/categories.html'