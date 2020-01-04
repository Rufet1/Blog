from django import forms
from .models import UserProfil
from django.contrib.auth.models import User

class ProfilForm(forms.ModelForm):
    class Meta:
        labels = {
            'image':'Profil şəkli'
        }
        model = UserProfil
        fields = [
            'image'
        ]

  