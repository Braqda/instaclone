from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import ChatRoom, Message

User = get_user_model()


@login_required
def chat_index(request):
    rooms = request.user.chat_rooms.all()
    return render(request, 'messaging/index.html', {'rooms': rooms})


@login_required
def start_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    room = ChatRoom.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not room:
        room = ChatRoom.objects.create()
        room.participants.add(request.user, other_user)

    return redirect('chat_room', room_id=room.id)


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Message.objects.create(room=room, sender=request.user, text=text)
        return redirect('chat_room', room_id=room.id)

    return render(request, 'messaging/room.html', {'room': room})
