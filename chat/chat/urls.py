from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('chat/', include('chatroom.urls')),
    path('admin/', admin.site.urls),
]
