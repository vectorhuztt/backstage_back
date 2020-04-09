from django.urls import path
from Api import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('label/', views.LabelView.as_view(), name='label'),
    path('users/', views.ListUserView.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]