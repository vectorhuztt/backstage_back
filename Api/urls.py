from django.urls import path
from Api import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserView.as_view(), name='login'),
]