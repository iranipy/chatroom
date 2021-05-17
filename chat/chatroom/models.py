from django.db import models


class PublicRoom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
