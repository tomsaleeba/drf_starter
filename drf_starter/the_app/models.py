from django.db import models

class User(models.Model):
    name = models.TextField()
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
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    upload = models.FileField(null=True)

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
