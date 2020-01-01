from django import forms
from .models import UserProfil
from django.contrib.auth.models import User

class ProfilForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = [
            'image'
        ]

  