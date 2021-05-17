from django.shortcuts import render

from .models import PublicRoom


def index(request):
    p_rooms = PublicRoom.objects.all().order_by('-id')
    return render(request, 'chatroom/index.html', context={'p_rooms': p_rooms})


def room(request, room_name):
    context = {
        'room_name': room_name
    }
    try:
        room_info = PublicRoom.objects.get(slug=room_name)
        context['room_info'] = room_info
    except PublicRoom.DoesNotExist:
        pass

    return render(request, 'chatroom/room.html', context=context)
