from django.contrib import admin

from .models import PublicRoom


class PublicRoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicRoom, PublicRoomAdmin)
