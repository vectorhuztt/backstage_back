from Api.models import LabelModel
from Api.serializers import LabelSerializer


class GetLabelData:

    def get_label_data(self, labels, data, count=1):
        for x in labels:
            label = LabelModel.objects.get(pk=x.id)
            serializer = LabelSerializer(label)
            children_data = serializer.data
            children_data['children'] = []
            data.append(children_data)
            children_labels = LabelModel.objects.filter(label_level=count, parent_id=x.id)
            self.get_label_data(children_labels, data=children_data['children'], count=count + 1)