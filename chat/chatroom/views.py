from django.shortcuts import render, redirect
from django.contrib import messages

from .models import PublicRoom, PrivateRoom
from .forms import PrivateRoomCreationForm, EnterPrivateRoom
from .utils import str_encryption


def index(request):
    request.session.flush()
    p_rooms = PublicRoom.objects.all().order_by('-id')
    return render(request, 'chatroom/index.html', context={'p_rooms': p_rooms})


def room(request, room_name):
    context = {
        'room_name': room_name
    }

    try:
        private_room = PrivateRoom.objects.get(name=room_name)

        cookie = request.session.get(room_name)
        if not cookie:
            return redirect('enter-private-room', room_name)
        cookie = cookie.encode()
        dec_cookie = str_encryption(cookie, dec=True)
        if not dec_cookie:
            return redirect('enter-private-room', room_name)
        if dec_cookie != room_name:
            return redirect('enter-private-room', room_name)
    except PrivateRoom.DoesNotExist:
        try:
            room_info = PublicRoom.objects.get(slug=room_name)
            context['room_info'] = room_info
        except PublicRoom.DoesNotExist:
            pass

        return render(request, 'chatroom/room.html', context=context)

    room_info = private_room
    context['room_info'] = room_info
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
            enc_name = str_encryption(room_name, enc=True)
            request.session[room_name] = enc_name.decode()
            messages.success(request, 'Welcome')
            return redirect('room', room_name)
    form = EnterPrivateRoom()
    return render(request, 'chatroom/enter_private_room.html', {'form': form})
