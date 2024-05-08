from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/post/', views.create_post, name='create_post'),
    path('index/', views.index, name='index'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('profile/', views.profile, name='profile'),
    path('blog/<int:id>/update', views.update_post, name='update_post'),
    path('blog/<int:id>/delete', views.delete_post, name='delete_post'),
]