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
]