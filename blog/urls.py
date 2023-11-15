from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list_posts.as_view(), name='index'),
    path('<int:pk>/', views.detail_post.as_view(), name='detail'),
    path('create/', views.create_post.as_view(), name='create'),
    path('update/<int:pk>/', views.update_post.as_view(), name='update'),
    path('delete/<int:pk>/', views.delete_post.as_view(), name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
]