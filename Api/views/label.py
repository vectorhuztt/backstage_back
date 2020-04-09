from rest_framework.response import Response
from rest_framework.views import APIView

from Api.models import LabelModel
from Api.serializers import LabelSerializer
from Api.utils.label_fomat import GetLabelData


class LabelView(APIView):
    def get(self, request):
        res = {
            'code': 200,
            'msg': '获取标签成功',
            'data': [],
        }
        first_labels = LabelModel.objects.filter(label_level=0)
        GetLabelData().get_label_data(first_labels, data=res['data'])
        return Response(data=res)