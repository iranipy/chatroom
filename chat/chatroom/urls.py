from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('private-chat/create/', views.create_private_room, name='private-room'),
    path('private-chat/enter/', views.enter_private_room, name='enter-private-room'),
]
