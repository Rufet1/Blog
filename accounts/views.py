from django.shortcuts import render,redirect, Http404
from .forms import LoginForm, RegisterForm,PasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from profil.models import UserProfil
from .models import Born
from django.db.models import Q
import datetime
# from .models import UserProfile
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return Http404
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login (request, user)
        return redirect('home')
    return render(request, 'accounts/login.html',{'form':form, 'title':'Daxil ol', 'basliq':'Giriş'})

def register_view(request):
    if request.user.is_authenticated:
        return Http404
    form = RegisterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        form.user = request.user
        user.first_name = form.cleaned_data.get('name')
        user.last_name = form.cleaned_data.get('surname')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username , password=password)
        login(request, new_user)
        born = form.cleaned_data.get('date')
        print('------------------------')
        print(born)
        user = request.user
        new_born_date = Born(user=user,date = born)
        new_born_date.save()        
        return redirect ('home')
    return render(request, 'accounts/register.html',{'form':form , 'title':'Qeydiyyatdan kec','basliq':'Qeydiyyat'})

# def born_date_register(request):
#     form = RegisterForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         born = form.cleaned_data.get('date').replace("/","-")
#         new_born = str(born[6:]+'-'+born[:2]+"-"+born[3:5])
#         print('------------------------')
#         print(new_born)
#         user = request.user
#         new_born_date = Born(user=user,date = new_born)
#         new_born_date.save()

def logout_view(request):
    if not request.user.is_authenticated:
        return Http404
    logout(request)
    return redirect ('home')

def password(request):
    form = PasswordForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        new_password2 = form.cleaned_data.get('newpassword1')
        new_password = form.cleaned_data.get('newpassword2')
        user = User.objects.get(username = request.user.username)
        if user.check_password(password) and new_password == new_password2:
            user.set_password(new_password)
            user.save()
            return redirect('accounts:login')
    return render(request,'accounts/password.html',{'form':form})






