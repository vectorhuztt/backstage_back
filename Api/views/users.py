import re
import uuid
from datetime import datetime

from django.db.models import Q
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import UserModel, UserToken, UserTypeModel
from Api.paginate import MyPageNumberPagination
from Api.serializers import UserSerializer, UserTypeSerializer


class RegisterUserView(APIView):
    """用户注册"""
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        res = {
            'code': 400,
            'msg': None
        }
        username = request._request.POST.get('username')
        password = request._request.POST.get('password')
        user_type = request._request.POST.get('user_type')
        user_phone = request._request.POST.get('userphone')
        user_email = request._request.POST.get('user_email')
        user = UserModel.objects.filter(username=username).first()
        user_by_phone = UserModel.objects.filter(userphone=user_phone).first()
        user_by_email = UserModel.objects.filter(user_email=user_email).first()
        if not password or not username:
            res['msg'] = '用户名或密码是必填选项'
            return Response(data=res)
        if not user_phone:
            res['msg'] = '手机号是必填选项'
            return Response(data=res)
        else:
            if not re.match(r'1[3-9]\d{9}$', user_phone):
                res['msg'] = '手机号非正常格式，请重新输入'
                return Response(data=res)
        if user_email:
            pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            if not pattern.match(user_email):
                res['msg'] = '邮箱格式不正确，请重新输入'
                return Response(data=res)
            else:
                if user_by_email:
                    res['msg'] = '邮箱已被注册，请更换其他邮箱'
                    return Response(data=res)
        if user:
            res['msg'] = '用户名已存在'
            return Response(data=res)
        if user_by_phone:
            res['msg'] = '该手机已被其他账号绑定，请更换其他手机号'
            return Response(data=res)

        if not user_type:
            user_type = 1
        else:
            if user_type not in ['1', '2', '3']:
                res['msg'] = 'user_type仅限在1|2|3之间'
                return Response(data=res)

        UserModel.objects.create(username=username, password=password,
                                 user_type_id=user_type, userphone=user_phone,
                                 user_email=user_email)
        user = UserModel.objects.filter(username=username).first()
        serializer = UserSerializer(user)
        res['code'] = 200
        res['msg'] = '添加用户成功'
        res['data'] = serializer.data
        return Response(data=res)


class LoginUserView(APIView):
    """用户登录获取token"""
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


class ListUserView(APIView):
    """获取用户列表"""
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        query = request._request.GET.get('query')
        print(query)
        pg = MyPageNumberPagination()
        data = {
            'code': 200,
            'msg': None
        }

        if query:
            users = UserModel.objects.filter(Q(username__icontains=query) |
                                             Q(user_email__icontains=query) |
                                             Q(userphone__contains=query))
        else:
            users = UserModel.objects.all().order_by('id')
        try:
            page_roles = pg.paginate_queryset(queryset=users, request=request, view=self)
            ser = UserSerializer(instance=page_roles, many=True)
            data['total'] = len(users)
            data['page_size'] = pg.page_size
            data['msg'] = '获取用户列表成功'
            data['data'] = ser.data
        except:
            data['code'] = 400
            data['msg'] = '获取用户列表失败'
        return Response(data=data)


class UserInfoView(APIView):
    """单个用户信息操作"""
    def get(self, request):
        """获取用户详细信息"""
        res = {
            'code': 200,
            'msg': None,
        }
        user_id = request._request.GET.get('id')
        user = UserModel.objects.filter(pk=user_id).first()
        if user:
            serializer = UserSerializer(user)
            res['msg'] = '获取用户信息成功'
            res['data'] = serializer.data
            return Response(data=res)
        else:
            res['code'] = 400
            res['msg'] = '用户不存在'
            return Response(data=res)

    def delete(self, request):
        """删除用户"""
        res = {
            'code': 400,
            'msg': None
        }
        user_id = request._request.GET.get('id')
        user = UserModel.objects.filter(pk=user_id).first()
        if not user:
            res['msg'] = '用户不存在'
            return Response(data=res)
        else:
            user.delete()
            res['msg'] = '删除用户成功'
            res['code'] = 200
            return Response(data=res)

    def put(self, request, *args, **kwargs):
        """更新用户状态"""
        res = {
            'code': 400,
            'msg': None
        }
        user_id = request._request.GET.get('id')
        status = request._request.GET.get('is_active')
        user_phone = request._request.GET.get('userphone')
        user_email = request._request.GET.get('user_email')
        user = UserModel.objects.filter(pk=user_id).first()
        user_by_phone = UserModel.objects.filter(userphone=user_phone).first()
        user_by_email = UserModel.objects.filter(user_email=user_email).first()
        if not user:
            res['msg'] = '用户不存在'
            return Response(data=res)
        else:
            if status:
                if status not in ['0', '1']:
                    res['msg'] = 'status 仅限0或1'
                    return Response(data=res)
                else:
                    user.is_active = status

            if user_phone:
                if user.userphone != user_phone:
                    if user_by_phone:
                        res['msg'] = '手机号已被注册，请重新输入'
                        return Response(data=res)
                    else:
                        if not re.match(r'1[3-9]\d{9}$', user_phone):
                            res['msg'] = '手机号非正常格式，请重新输入'
                            return Response(data=res)
                        else:
                            user.userphone = user_phone

            if user_email:
                if user.user_email != user_email:
                    if user_by_email:
                        res['msg'] = '邮箱已被注册， 请重新输入'
                    else:
                        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
                        if not pattern.match(user_email):
                            res['msg'] = '邮箱格式不正确，请重新输入'
                            return Response(data=res)
                        else:
                            user.user_email = user_email
            time = datetime.now()
            user.updated_time = time
            user.save()
            res['code'] = 200
            res['msg'] = '更新用户信息成功'
        return Response(data=res)


class UserTypeView(APIView):
    """用户类型列表"""
    def get(self, request):
        res = {
            'code': 200,
            'msg': None
        }
        try:
            user_types = UserTypeModel.objects.all()
            serializer = UserTypeSerializer(user_types, many=True)
            res['msg'] = '获取用户类型列表成功'
            res['data'] = serializer.data
        except Exception as e:
            res['code'] = 400
            res['msg'] = str(e)
        return Response(data=res)
