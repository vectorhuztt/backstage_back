from Api.models import LabelModel, ApiModel
from Api.serializers import LabelSerializer


class GetLabelData:

    def get_label_data(self, labels, data, count=1):
        """获取标签数据"""
        for x in labels:
            label = LabelModel.objects.get(pk=x.id)
            serializer = LabelSerializer(label)
            children_data = serializer.data
            pid = children_data['pid']
            api_model = ApiModel.objects.filter(pid=pid).first()
            if api_model:
                children_data['path'] = api_model.path
            children_data.pop('pid')
            children_data['children'] = []
            data.append(children_data)
            children_labels = LabelModel.objects.filter(label_level=count, parent_id=x.id)
            self.get_label_data(children_labels, data=children_data['children'], count=count + 1)

    def get_role_label_data(self, role_children, label_ids, parent_id):
        """将权限树形数据嵌套在角色的子集中"""
        for x in label_ids:
            label = LabelModel.objects.filter(pk=x).first()
            if label.parent_id == parent_id:
                label_serializer = LabelSerializer(label)
                label_data = label_serializer.data
                label_data['children'] = []
                role_children.append(label_data)
                self.get_role_label_data(label_data['children'], label_ids, label.id)

    @classmethod
    def remove_role_label_ids(cls, role_label_ids, id_list, label_id, label_level):
        """移除用户的权限列表id"""
        if label_level != 2:
            for x in role_label_ids:
                second_label = LabelModel.objects.filter(pk=x).first()
                if second_label.parent_id == int(label_id):
                    id_list.remove(int(x))
                if label_level == 0:
                    for y in id_list.copy():
                        third_label = LabelModel.objects.filter(pk=x).first()
                        if third_label.parent_id == int(x):
                            id_list.remove(int(x))
        id_list.remove(int(label_id))



