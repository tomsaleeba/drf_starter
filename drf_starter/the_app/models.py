from uuid import uuid1
from django.db import models


def get_uuid(instance, filename):
    return str(uuid1())


class User(models.Model):
    first_name = models.TextField()
    surname = models.TextField()
    location = models.ForeignKey(
        'Location',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    groups = models.ManyToManyField(
        'Group',
        related_name='users',
        blank=True,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    data = models.ImageField(upload_to=get_uuid, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.TextField(unique=True)
    location = models.ForeignKey(
        'Location',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
