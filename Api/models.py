from django.db import models


class UserModel(models.Model):
    user_type_choice = (
        (1, 'normal_user'),
        (2, 'manager_user'),
        (3, 'super_user')
    )

    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=128)
    user_type = models.IntegerField(choices=user_type_choice, default=1)

    class Meta:
        db_table = 'user_model'


class UserToken(models.Model):
    user = models.OneToOneField(to='UserModel', on_delete=models.CASCADE)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'user_token'


class LabelModel(models.Model):
    label_name = models.CharField(max_length=10)
    parent_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'label'