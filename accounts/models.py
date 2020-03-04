from django.db import models
from django.contrib.auth.models import User

class Born(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateField(default='2020-02-20')
