from django.db import models

from .utils import uid_gen


class PublicRoom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class PrivateRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)
    room_uid = models.CharField(default=uid_gen, max_length=36, editable=False, unique=True)
    description = models.TextField()
    capacity = models.IntegerField(null=True, blank=True)
