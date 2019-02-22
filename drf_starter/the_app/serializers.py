from rest_framework import serializers as rf_serializers
from dynamic_rest import fields
from dynamic_rest import serializers
from drf_extra_fields.fields import HybridImageField

from drf_starter.the_app.models import (
    User,
    Group,
    Location,
)
from drf_starter.the_app.fields import (
    UserNameField,
    UserFirstNameField,
    UserSurnameField,
    compute_first_name,
    compute_surname,
)


class UserBaseSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = User
        name = 'user'
        fields = ('id', 'location', 'groups', 'data', 'uploaded_at')
        read_only_fields = ('uploaded_at',)

    location = fields.DynamicRelationField('LocationSerializer', embed=True)
    groups = fields.DynamicRelationField('GroupSerializer', many=True, deferred=True, embed=True)
    data = HybridImageField(required=False)


class UserV1Serializer(UserBaseSerializer):
    class Meta(UserBaseSerializer.Meta):
        fields = ('name',) + UserBaseSerializer.Meta.fields

    name = UserNameField()

    def create(self, validated_data):
        name_value = validated_data.pop('name')
        validated_data['first_name'] = compute_first_name(name_value)
        validated_data['surname'] = compute_surname(name_value)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name_value = validated_data.pop('name')
        instance.first_name = compute_first_name(name_value)
        instance.surname = compute_surname(name_value)
        instance.save()
        return instance


class UserV2Serializer(UserBaseSerializer):
    class Meta(UserBaseSerializer.Meta):
        fields = ('first_name', 'surname') + UserBaseSerializer.Meta.fields

    first_name = UserFirstNameField()
    surname = UserSurnameField()


class LocationSerializer(serializers.DynamicModelSerializer):
    class Meta:
        defer_many_relations = False
        model = Location
        name = 'location'
        fields = ('id', 'name', 'users')

    users = serializers.DynamicRelationField(
        UserV2Serializer, # ideally we would have two versions of Location to match User
        source='user_set',
        many=True,
        deferred=True,
        embed=True,
    )


class GroupSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = Group
        name = 'group'
        fields = ('id', 'name', 'location', 'users')

    location = fields.DynamicRelationField(LocationSerializer, embed=True)
    # TODO this field may explode in the browsable API because the generated form sends null by default
    # if we could get our field into
    # https://github.com/encode/django-rest-framework/blob/master/rest_framework/renderers.py#L267 then we can control
    # what it gets rendered like. Currently it's treated as just Field.
    # This alternative presents nicely in the browsable API but doesn't have the nested capability:
    #    users = rf_serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    # Otherwise if this field can handle null, all will be well.
    users = fields.DynamicRelationField(
        UserV2Serializer, # ideally we would have two versions of Group to match User
        many=True,
        deferred=True,
        embed=True,
    )

