from django.urls import path
from auth_Login import views


urlpatterns = [
    path('login', views.loginUser, name="auth_Login_login"),
]
