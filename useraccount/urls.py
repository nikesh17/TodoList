from django.urls import path
from useraccount.views import UserLoginView, SignUpView
from django.contrib.auth.views import LogoutView

app_name="user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),
]
