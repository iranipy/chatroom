from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PublicRoom, PrivateRoom
from .forms import PrivateRoomCreationForm, EnterPrivateRoom


def index(request):
    p_rooms = PublicRoom.objects.all().order_by('-id')
    return render(request, 'chatroom/index.html', context={'p_rooms': p_rooms})


def room(request, room_name):
    try:
        private_room = PrivateRoom.objects.get(name=room_name)
        return redirect('enter-private-room', room_name)
    except PrivateRoom.DoesNotExist:
        pass
    context = {
        'room_name': room_name
    }

    try:
        room_info = PublicRoom.objects.get(slug=room_name)
        context['room_info'] = room_info
    except PublicRoom.DoesNotExist:
        pass
    try:
        room_info = PrivateRoom.objects.get(room_uid=room_name)
        context['room_info'] = room_info
    except PrivateRoom.DoesNotExist:
        pass

    return render(request, 'chatroom/room.html', context=context)


def create_private_room(request):
    if request.method == 'POST':
        form = PrivateRoomCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            PrivateRoom.objects.create(**form.cleaned_data).save()
            messages.success(request, f'{name} room created')
            return redirect('room', name)
    form = PrivateRoomCreationForm()
    return render(request, 'chatroom/create_private_room.html', {'form': form})


def enter_private_room(request, room_name):
    if request.method == 'POST':
        form = EnterPrivateRoom(request.POST)
        if form.is_valid():
            private_room = PrivateRoom.objects.get(name=room_name)
            password = form.cleaned_data.get('password')
            if private_room.password != password:
                messages.error(request, 'Wrong')
                return redirect('enter-private-room', room_name)
            messages.success(request, 'Welcome')
            return redirect('room', room_name)
    form = EnterPrivateRoom()
    return render(request, 'chatroom/enter_private_room.html', {'form': form})
