from django.forms import ModelForm

from .models import Post


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
            'data_de_postagem': 'Data de Postagem',
            'conteúdo': 'Conteúdo',
        }