from django.db import models

class UserTypeModel(models.Model):
    type_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'user_type'


class UserModel(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=128)
    userphone = models.CharField(max_length=15, unique=True)
    user_email = models.CharField(max_length=128, null=True, unique=True)
    user_type = models.ForeignKey("UserTypeModel", to_field='id', related_name='user_type', on_delete=models.CASCADE)
    created_time = models.DateTimeField(null=True, auto_now_add=True)
    updated_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_model'


class UserToken(models.Model):
    user = models.OneToOneField(to='UserModel', on_delete=models.CASCADE)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'user_token'


class ApiModel(models.Model):
    pid = models.IntegerField()
    path = models.CharField(max_length=64)
    desc = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'api_model'


class LabelModel(models.Model):
    label_level_choice = (
        (1, 'first_level'),
        (2, 'second_level'),
        (3, 'third_level')
    )
    label_name = models.CharField(max_length=10)
    parent_id = models.IntegerField(default=0)
    label_level = models.IntegerField(choices=label_level_choice, default=1)
    icon_class = models.CharField(max_length=128, null=True)
    pid = models.IntegerField(default=0)

    class Meta:
        db_table = 'label'