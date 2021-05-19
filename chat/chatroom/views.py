from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PublicRoom, PrivateRoom
from .forms import PrivateRoomCreationForm, EnterPrivateRoom


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
            room = PrivateRoom.objects.create(**form.cleaned_data).save()
            room_uid = PrivateRoom.objects.get(name=name).room_uid
            messages.success(request, f'{name} room created')
            return redirect('room', room_uid)
    form = PrivateRoomCreationForm()
    return render(request, 'chatroom/create_private_room.html', {'form': form})


def enter_private_room(request):
    if request.method == 'POST':
        form = EnterPrivateRoom(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('roomname')
            try:
                room = PrivateRoom.objects.get(name=name)
            except PrivateRoom.DoesNotExist:
                messages.error(request, 'not found!')
                return redirect('enter-private-room')
            password = form.cleaned_data.get('password')
            if room.password != password:
                messages.error(request, 'Password is wrong!')
                return redirect('enter-private-room')
            return redirect('room', room.room_uid)

    form = EnterPrivateRoom()
    return render(request, 'chatroom/enter_private_room.html', {'form': form})
