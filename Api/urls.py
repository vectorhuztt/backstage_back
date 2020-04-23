from django.urls import path
from rest_framework.documentation import include_docs_urls

from Api import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('label/', views.LabelView.as_view(), name='label-tree'),
    path('types/', views.UserTypeView.as_view(), name='types'),
    path('users/', views.ListUserView.as_view(), name='users'),
    path('user-action/', views.UserInfoView.as_view(), name='user-action'),
    path('roles/', views.get_roles, name="role"),
    path('roles/remove-label/', views.remove_label_id, name='role-remove-label'),
    path('roles/update-label/', views.update_role_label_ids, name='role-update-label'),
    path('roles/create-role/', views.create_roles, name='create-role'),
    path('roles/update-role/', views.update_roles, name='update-role'),
    path('roles/delete-role/', views.delete_roles, name='delete-role'),
    path('roles/detail/', views.role_detail, name="role-detail")
]