from dynamic_rest import fields
from dynamic_rest import serializers
from drf_extra_fields.fields import HybridImageField

from drf_starter.the_app import models

class UserSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.User
        name = 'user'
        fields = ('id', 'name', 'location', 'groups', 'data', 'uploaded_at')
        read_only_fields = ('uploaded_at',)

    location = fields.DynamicRelationField('LocationSerializer', embed=True)
    groups = fields.DynamicRelationField('GroupSerializer', many=True, deferred=True, embed=True)
    data = HybridImageField(required=False)


class GroupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Group
        name = 'group'
        fields = ('id', 'name', 'location', 'users')

    location = fields.DynamicRelationField('LocationSerializer', embed=True)
    users = fields.DynamicRelationField('UserSerializer', many=True, deferred=True, embed=True)

class LocationSerializer(serializers.DynamicModelSerializer):

    class Meta:
        defer_many_relations = False
        model = models.Location
        name = 'location'
        fields = (
            'id', 'name', 'users', 'user_count',
        )

    users = serializers.DynamicRelationField(
        'UserSerializer',
        source='user_set',
        many=True,
        deferred=True,
        embed=True,
    )
    user_count = fields.CountField('users', required=False, deferred=True)

