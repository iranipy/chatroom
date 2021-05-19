from django.contrib import admin

from .models import PublicRoom, PrivateRoom


class PublicRoomAdmin(admin.ModelAdmin):
    pass


class PrivateRoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicRoom, PublicRoomAdmin)
admin.site.register(PrivateRoom, PrivateRoomAdmin)
