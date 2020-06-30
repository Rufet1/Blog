from django.shortcuts import render,redirect,Http404
from .models import UserProfil
from .forms import ProfilForm
from django.contrib.auth.models import User
from accounts.forms import UpdateProfilForm
# Create your views here.

def add_image(request):
    form = ProfilForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        deletedimage = UserProfil.objects.filter(user=request.user).exists()
        if deletedimage == True:
            delimage = UserProfil.objects.get(user=request.user)
            delimage.delete()
            image = form.cleaned_data.get('image')
            newpic = UserProfil(user=request.user,image=image)
            newpic.save()
        else:
            image = form.cleaned_data.get('image')
            newpic = UserProfil(user=request.user,image=image)
            newpic.save()
    return render (request, 'profil/form.html', {'form':form, 'basliq':'Profil şəkli'})

def profil_view(request):
    if not request.user.is_authenticated:
        return Http404
    return render(request,'profil/profil.html')

def profiles(request):
    profiles = User.objects.all()
    return render(request,'profil/index.html', {'profiles':profiles})

def contact(request):
    return render(request, 'contact.html')

def update_profile(request):
    form = UpdateProfilForm(request.POST or None ,request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
    return render(request,'profil/updateprofile.html', {'form':form})