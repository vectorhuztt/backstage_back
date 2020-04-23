from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import RoleModel, LabelModel
from Api.serializers import RoleSerializer, LabelSerializer
from Api.utils.label_fomat import GetLabelData


@api_view(http_method_names=['post'])
def create_roles(request):
    """创建角色"""
    res = {
        'code': 200,
        'msg': None
    }
    role_name = request.POST.get('role_name')
    role_desc = request.POST.get('role_desc')
    try:
        role = RoleModel.objects.filter(role_name=role_name).first()
        if role:
            res['code'] = 400
            res['msg'] = '角色名称已存在'
            return Response(res)
        role = RoleModel.objects.create(role_name=role_name, role_desc=role_desc)
        serializer = RoleSerializer(role)
        res['data'] = serializer.data
        res['msg'] = '创建角色成功'
    except Exception as e:
        res['code'] = 400
        res['error'] = str(e)
        res['msg'] = '创建角色失败'
    return Response(res)


@api_view(http_method_names=['post'])
def update_roles(request):
    """更改角色信息"""
    res = {
        'code': 200,
        'msg': None
    }
    role_id = request.POST.get('id')
    role_name = request.POST.get('role_name')
    role_desc = request.POST.get('role_desc')
    try:
        role = RoleModel.objects.filter(pk=role_id).first()
        if not role:
            res['msg'] = '用户不存在'
            return Response(res)
        if role_name != role.role_name:
            exited_role = RoleModel.objects.filter(role_name=role_name).first()
            if exited_role:
                res['code'] = 400
                res['msg'] = '角色名称已存在'
                return Response(res)
        role.role_name = role_name
        role.role_desc = role_desc
        role.save()
        serializer = RoleSerializer(role)
        res['data'] = serializer.data
        res['msg'] = '更改角色信息成功'
    except Exception as e:
        res['code'] = 400
        res['error'] = str(e)
        res['msg'] = '更改角色信息失败'
    return Response(res)


@api_view(http_method_names=['get'])
def get_roles(request):
    """获取角色列表 带有权限列表"""
    res = {
        'code': 200,
        'msg': None
    }
    try:
        roles = RoleModel.objects.all()
        role_serializer = RoleSerializer(roles, many=True)
        role_data = role_serializer.data
        for role in role_data:
            role['children'] = []
            if not role['label_ids']:
                continue
            else:
                role_label_ids = role['label_ids'].split(',')
                GetLabelData().get_role_label_data(role['children'], role_label_ids, parent_id=0)
        res['data'] = role_data
        res['msg'] = '获取角色列表成功'
    except Exception as e:
        res['error'] = str(e)
        res['msg'] = '获取角色列表失败'
        res['code'] = 400
    return Response(data=res)


@api_view(http_method_names=['post'])
def remove_label_id(request):
    """删除角色权限"""
    role_id = request.POST.get('role_id')
    label_id = request.POST.get('label_id')
    res = {
        'code': 400,
        'msg': None
    }
    try:
        role = RoleModel.objects.filter(pk=role_id).first()   # 角色对象
        role_label_ids = role.label_ids.split(',')    # 角色拥有标签id
        final_label_list = [int(x) for x in role_label_ids]
        label = LabelModel.objects.filter(pk=label_id).first()  # 删除的标签id
        if not role:
            res['msg'] = '角色不存在'
            return Response(res)
        if not label:
            res['msg'] = '标签id不存在'
            return Response(res)
        if label_id not in role_label_ids:
            res['msg'] = '该角色不具有此权限'
            return Response(res)
        GetLabelData.remove_role_label_ids(role_label_ids, final_label_list, label_id, label.label_level)
        role.label_ids = ','.join([str(x) for x in final_label_list])
        role.save()
        serializer = RoleSerializer(role)
        role_data = serializer.data
        role_data['children'] = []
        GetLabelData().get_role_label_data(role_data['children'], final_label_list, parent_id=0)
        res['code'] = 200
        res['msg'] = '删除角色权限成功'
        res['data'] = role_data['children']
    except:
        res['msg'] = '删除角色权限失败'
    return Response(data=res)


@api_view(http_method_names=['post'])
def update_role_label_ids(request):
    """更新角色权限"""
    role_id = request.POST.get('role_id')
    id_str = request.POST.get('label_ids')
    res = {
        'code': 400,
        'msg': None
    }
    try:
        role = RoleModel.objects.filter(pk=role_id).first()  # 角色对象
        if not role:
            res['msg'] = '角色不存在'
            return Response(res)
        role.label_ids = id_str
        role.save()
        res['code'] = 200
        res['msg'] = '角色权限更新成功'
    except:
        res['msg'] = '角色权限更新失败'
    return Response(res)


@api_view(http_method_names=['post'])
def delete_roles(request):
    """删除角色"""
    res = {
        'code': 200,
        'msg': None
    }
    role_id = request.POST.get('role_id')
    try:
        role = RoleModel.objects.filter(pk=role_id).first()
        if not role:
            res['msg'] = '角色不存在'
            return Response(res)
        role.delete()
        res['msg'] = '删除角色成功'
    except Exception as e:
        res['code'] = 400
        res['error'] = str(e)
        res['msg'] = '删除角色失败'
    return Response(res)


@api_view(http_method_names=['get'])
def role_detail(request):
    """获取单个角色信息(不带权限)"""
    role_id = request.GET.get('id')
    print(role_id)
    res = {
        'code': 200,
        'msg': None
    }
    try:
        role = RoleModel.objects.filter(pk=role_id).first()
        if not role:
            res['code'] = 400
            res['msg'] = '用户不存在'
            return Response(res)
        serializer = RoleSerializer(role)
        res['msg'] = '获取角色信息成功'
        res['data'] = serializer.data
    except:
        res['msg'] = '获取角色信息失败'
    return Response(res)