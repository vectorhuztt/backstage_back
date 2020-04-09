from rest_framework.views import APIView

from Api.models import LabelModel
from Api.serializers import LabelSerializer


class LabelView(APIView):
    def get(self, request):
        res = {
            'code': 200,
            'msg': None,
            'data': {},
        }
        first_labels = LabelModel.objects.filter(label_level=0)
        index = 0
        for x in first_labels:
            label = LabelModel.objects.get(pk=x.id)
            serializer = LabelSerializer(label)
            res['data'][x.id] = serializer.data
            res['data'][x.id]['children'] = []
            second_labels = LabelModel.objects.filter(label_level=1, parent_id=x.id)

            for y in second_labels:
                label = LabelModel.objects.get(pk=y.id)
                serializer = LabelSerializer(label)
                data = serializer.data
                data['children'] = []
                res['data'][x.id]['children'].append(data)
                third_labels = LabelModel.objects.filter(label_level=2, parent_id=y.id)

                for z in third_labels:
                    label = LabelModel.objects.get(pk=z.id)
                    serializer = LabelSerializer(label)
                    data = serializer.data
                    res['data'][x.id]['children'][index]['children'].append(data)
                index += 1

        return Response(data=res)