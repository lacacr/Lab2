from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post

# Create your views here.

def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'blog/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_título = request.POST['título']
        post_data_de_postagem = request.POST['data_de_postagem']
        post_conteúdo = request.POST['conteúdo']
        post = Post(título=post_título,
                      data_de_postagem=post_data_de_postagem,
                      conteúdo=post_conteúdo)
        post.save()
        return HttpResponseRedirect(
            reverse('blog:detail', args=(post.id, )))
    else:
        return render(request, 'blog/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.título = request.POST['título']
        post.data_de_postagem = request.POST['data_de_postagem']
        post.conteúdo = request.POST['conteúdo']
        post.save()
        return HttpResponseRedirect(
            reverse('blog:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'blog/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('blog:index'))

    context = {'post': post}
    return render(request, 'blog/delete.html', context)