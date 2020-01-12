from django.shortcuts import render, redirect, Http404
from django.core.mail import send_mail
import random
from .forms import EmailForm,ForgetForm
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


def forget_view(request):
    all_emails = []
    all_usernames = []
    form = ForgetForm(request.POST or None)
    if form.is_valid():
        input = form.cleaned_data.get('input')
        for i in User.objects.all():
            all_emails.append(i.email)
            all_usernames.append(i.username)
        if input in all_emails:
            list = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            length = 8
            password = "".join(random.sample(list,length))
            print(password)
            send_mail('Jafarzada.com',
            password,
            'rufet.quliyev@hushmail.com',
            [input],
            fail_silently=False)
            user = User.objects.get(email = input)
            user.set_password(password)
            user.save()
            return redirect('sendemail:sentemail')
        elif input in all_usernames:
            user = User.objects.get(username = input)
            list = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            length = 8
            password = "".join(random.sample(list,length))
            print(password)
            send_mail('Jafarzada.com',
            password,
            'rufet.quliyev@hushmail.com',
            [user.email],
            fail_silently=False)
            user.set_password(password)
            user.save()
            return redirect('sendemail:sentemail')
    return render (request, 'accounts/password.html', {'form':form})



def email_sent(request):
    return render(request, 'accounts/sended.html')
        