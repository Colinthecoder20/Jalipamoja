from django.shortcuts import render

from chat.models import Room

def all_rooms_view(request): 
  rooms = Room.objects.all()
  
  return render(request, 'index.html', {
    'rooms': rooms
  })
  
def room_view(request, room_name): 
  chat_room, created = Room.objects.get_or_create(name=room_name)
  return render(request, 'room.html', {
    'room': chat_room,
  })