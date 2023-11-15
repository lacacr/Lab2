from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list_posts, name='index'),
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('create/', views.create_post, name='create'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]