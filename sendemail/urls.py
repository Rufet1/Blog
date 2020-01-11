from django.urls import path, re_path
from .views import * 
from django.conf.urls import url

app_name = "sendemail"

urlpatterns = [
 path('index', email_view, name="sendemail"),

]