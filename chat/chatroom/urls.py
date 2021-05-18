from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('create/private-room/', views.create_private_room, name='private-room'),
]
