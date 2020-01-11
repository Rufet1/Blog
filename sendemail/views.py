from django.shortcuts import render, redirect, Http404
from django.core.mail import send_mail
import random
from .forms import EmailForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def email_view(request):
    if not request.user.is_authenticated:
        return Http404
    list = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    length = 8
    password = "".join(random.sample(list,length))
    print(password)
    send_mail('Jafarzada.com',
    password,
    'rufet.quliyev@hushmail.com',
    [request.user.email],
    fail_silently=False)
    user = User.objects.get(username=request.user.username)
    user.set_password(password)
    user.save()
    logout(request)
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     sentemail = form.cleaned_data.get('sentemail')
    #     print(sentemail)
    #     print(password)
    #     if sentemail == password:
    #         redirect ('home')
    #         print('isledi')
    #     else:
    #         print('islemedi')
    return render (request,'sendemail/index.html')