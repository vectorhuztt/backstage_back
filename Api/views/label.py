from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import LabelModel, ApiModel
from Api.paginate import MyPageNumberPagination
from Api.serializers import LabelSerializer
from Api.utils.label_fomat import GetLabelData


class LabelView(APIView):
    def get(self, request):
        data_type = request._request.GET.get('type')
        page = request._request.GET.get('page')
        if not data_type:
            data_type = 'tree'
        res = {
            'code': 200,
            'msg': None,
        }
        try:
            if data_type in ['tree', 'list']:
                data_list = []
                if data_type == 'tree':
                    first_labels = LabelModel.objects.filter(label_level=0)
                    GetLabelData().get_label_data(first_labels, data=data_list)
                else:
                    labels = LabelModel.objects.all()
                    if page:
                        pg = MyPageNumberPagination()
                        page_roles = pg.paginate_queryset(queryset=labels, request=request, view=self)
                    else:
                        page_roles = labels
                    for x in page_roles:
                        ser = LabelSerializer(instance=x)
                        data = ser.data
                        pid = data['pid']
                        api_model = ApiModel.objects.filter(pid=pid).first()
                        if api_model:
                            data['path'] = api_model.path
                        else:
                            data['path'] = None
                        data_list.append(data)
                    res['total'] = len(labels)
                res['data'] = data_list
                res['msg'] = '获取标签成功'
            else:
                res['code'] = 400
                res['msg'] = 'type参数仅接受tree | list'
        except:
            res['code'] = 400
            res['msg'] = '获取标签失败'
        return Response(data=res)


