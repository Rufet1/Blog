from django.urls import path, re_path
from .views import * 
from django.conf.urls import url

app_name = "profile"

urlpatterns = [
    path('profileimage', add_image, name="profilimage"),
    path('profile', profil_view,name='profil'),
    path('index', profiles, name='profiles'),
]