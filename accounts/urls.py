from django.urls import path, re_path
from .views import * 
from django.conf.urls import url

app_name = "accounts"

urlpatterns = [
 path('login', login_view, name="login"),
 path('register', register_view, name="register"),
 path('logout', logout_view, name="logout"),
]