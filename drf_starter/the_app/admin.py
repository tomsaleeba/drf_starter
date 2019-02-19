from django.contrib import admin
from drf_starter.the_app.models import User, Group, Location

admin.site.register(Group)
admin.site.register(Location)
admin.site.register(User)
