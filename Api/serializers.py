from rest_framework import serializers

from Api.models import UserModel, LabelModel, ApiModel, UserTypeModel


class UserSerializer(serializers.ModelSerializer):
    user_type_name = serializers.CharField(source='user_type.type_name')
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'userphone': {'required': True},
        }
        model = UserModel
        exclude = ['password', 'updated_time']


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = ('id', 'path')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelModel
        fields = ('id', 'label_name', 'label_level', 'icon_class', 'pid')


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypeModel
        fields = '__all__'