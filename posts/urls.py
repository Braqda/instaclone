from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
