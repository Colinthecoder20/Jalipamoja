from django.urls import path 

from . import views

urlpatterns = [
  path('', views.all_rooms_view, name='chat-index'),
  path('<str:room_name>/', views.room_view, name='chat-room')
]