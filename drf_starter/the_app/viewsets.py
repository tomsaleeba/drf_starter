from rest_framework.exceptions import NotAcceptable
from dynamic_rest import viewsets

from drf_starter.the_app import models
from drf_starter.the_app import serializers


class UserViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.UserBaseSerializer
    queryset = models.User.objects.all()
    ordering = ('-id',)

    def get_serializer_class(self):
        default_version = '2'
        the_version = self.request.version or default_version
        handlers = {
            '1': serializers.UserV1Serializer,
            '2': serializers.UserV2Serializer,
        }
        try:
            return handlers[the_version]
        except KeyError as e:
            raise NotAcceptable(detail="Supplied version '%s' is not supported. Valid versions are %s" % (the_version,
                str(list(handlers.keys()))))


class GroupViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    ordering = ('-id',)


class LocationViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    ordering = ('-id',)
