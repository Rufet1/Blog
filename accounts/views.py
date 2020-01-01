from django.shortcuts import render,redirect, Http404
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from profil.models import UserProfil
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
        profilimage = UserProfil(user=user , image='default.jpg')
        profilimage.save()
        
        return redirect ('home')
    return render(request, 'accounts/register.html',{'form':form , 'title':'Qeydiyyatdan kec','basliq':'Qeydiyyat'})

def logout_view(request):
    if not request.user.is_authenticated:
        return Http404
    logout(request)
    return redirect ('home')

