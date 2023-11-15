from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'título',
            'data_de_postagem',
            'conteúdo',
        ]
        labels = {
            'título': 'Título',
            'data_da_postagem': 'Data da Postagem',
            'conteúdo': 'Conteúdo',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'data_da_postagem',
            'texto'
        ]
        labels = {
            'autor': 'Autor',
            'data_da_postagem': 'Data da Postagem',
            'texto': 'Texto'
        }    