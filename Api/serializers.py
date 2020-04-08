from  rest_framework import serializers

from Api.models import UserModel, LabelModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        extra_kwargs = {
            'url': {'view_name': 'api:user-detail'},
            'username': {'required': True},
            'password': {'required': True},
        }
        model = UserModel
        fields = ('urls', 'username', 'user_type')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelModel
        fields = ('id', 'label_name', 'parent_id')