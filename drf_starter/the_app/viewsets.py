from rest_framework.exceptions import NotAcceptable
from dynamic_rest import viewsets

from drf_starter.the_app import models
from drf_starter.the_app import serializers

def only_one_version_handler(version, the_serializer):
    default_version = '1'
    the_version = version or default_version
    try:
        assert the_version == '1'
        return the_serializer
    except AssertionError:
        raise NotAcceptable(detail="Supplied version '%s' is not supported. Valid versions are %s" % (the_version,
            str(list(default_version))))

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

    def get_serializer_class(self):
        return only_one_version_handler(self.request.version, serializers.GroupSerializer)


class LocationViewSet(viewsets.DynamicModelViewSet):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    ordering = ('-id',)

    def get_serializer_class(self):
        return only_one_version_handler(self.request.version, serializers.LocationSerializer)
