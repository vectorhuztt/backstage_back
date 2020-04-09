import uuid

from rest_framework import exceptions
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import UserModel, UserToken
from Api.serializers import UserSerializer


class RegisterUserView(APIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

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
        else:
            if user_type not in [1, 2, 3]:
                return Response({'error': 'user_type仅限在1|2|3之间'})
        UserModel.objects.create(username=username, password=password, user_type=user_type)
        data = {
            'msg': '注册成功',
            'data': {
                'username': username,
                'user_type': user_type
            }
        }
        return Response(data=data)


class LoginUserView(APIView):
    authentication_classes = []
    permission_classes = []

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


class ListUserView(ListAPIView):
    """获取用户列表"""
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,  *args, **kwargs)