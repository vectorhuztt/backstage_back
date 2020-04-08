import uuid

from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import UserModel, UserToken
from Api.serializers import UserSerializer


class RegisterView(APIView):
    serializer_class = UserSerializer
    authentication_classes = []

    def post(self, request):
        username = request._request.POST.get('username')
        password = request._request.POST.get('password')
        user_type = request._request.POST.get('user_type')
        user = UserModel.objects.filter(username=username).first()
        if user:
            return Response({'error': '用户已存在'})
        if not password or not username:
            return Response({'error': '用户名或密码是必填选项'})
        if not user_type:
            user_type = 1
        UserModel.objects.create(username=username, password=password, user_type=user_type)
        data = {
            'msg': '注册成功',
            'data': {
                'username': username,
                'user_type': user_type
            }
        }
        return Response(data=data)


class UserView(APIView):
    authentication_classes = []

    def post(self, request):
        data = {
            "code": 200,
            "msg": None
        }
        try:
            username = request._request.POST.get('username')
            password = request._request.POST.get('password')
            user = UserModel.objects.filter(username=username, password=password).first()
            if not user:
                data['code'] = 400,
                data['msg'] = '用户名或密码错误'
            else:
                token = uuid.uuid4().hex
                data['username'] = username
                data['token'] = token
                data['msg'] = '登录成功'
                UserToken.objects.update_or_create(user=user, defaults={'token': token})
        except Exception:
            raise exceptions.ValidationError
        return Response(data=data)


class LabelView(APIView):

    def get(self, request):
        pass