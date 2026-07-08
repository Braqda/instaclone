from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_index, name='chat_index'),
    path('start/<int:user_id>/', views.start_chat, name='start_chat'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
]

