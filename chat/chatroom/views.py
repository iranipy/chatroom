from django.shortcuts import render
import uuid


def index(request):
    context = {
        'uid': uuid.uuid4()
    }
    return render(request, 'chatroom/index.html', context=context)

def room(request, room_name):
    return render(request, 'chatroom/room.html', {
        'room_name': room_name
    })