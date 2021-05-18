from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import PublicRoom, PrivateRoom
from .forms import PrivateRoomCreationForm


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


def create_private_room(request):
    if request.method == 'POST':
        form = PrivateRoomCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            slug = form.cleaned_data.get('slug')

            messages.success(request, f'{name} room created')
            return redirect('room', slug)
    form = PrivateRoomCreationForm()
    return render(request, 'chatroom/create_private_room.html', {'form': form})
