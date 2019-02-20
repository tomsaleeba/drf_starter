from dynamic_rest import viewsets

from drf_starter.the_app import models
from drf_starter.the_app import serializers

class UserViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    ordering = ('-id',)


class GroupViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    ordering = ('-id',)


class LocationViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    ordering = ('-id',)
