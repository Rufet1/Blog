from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from profil.models import UserProfil
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='İstifadəçi adı')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput,label='Parol')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username veya parolu sehv daxil etdiniz!')
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='İstifadəçi adı')
    name = forms.CharField(max_length=100, label='Ad' )
    surname = forms.CharField(max_length=100,label='Soyad')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput,label='Parol')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parol (təkrar)')
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'surname',
            'password1',
            'password2',
            'email',
        ]
        


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!= password2:
            raise forms.ValidationError('Parollar eyni deyil!')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        all_user = User.objects.all()
        email_list = []
        for i in all_user:
            email_list.append(i.email)
        for user in all_user:
            if email in email_list:
                raise forms.ValidationError('daxil etdiyiniz email movcuddur!') 
            return email

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=255,widget=forms.PasswordInput,label='İndiki Parolunuz')
    newpassword1 = forms.CharField(max_length=255,widget=forms.PasswordInput,label='Yeni Parol')
    newpassword2 = forms.CharField(max_length=255,widget=forms.PasswordInput,label='Yeni parol (təkrar)')
    

    def clean_newpassword2(self):
        new_password2 = self.cleaned_data.get('newpassword1')
        new_password = self.cleaned_data.get('newpassword2') 
        if new_password2 and new_password and new_password2 != new_password:
            raise forms.ValidationError('Parollar eyni deyil!')
        return new_password2      

    # def clean_password(self):
    #      password = self.cleaned_data.get('password')
    #      if password and User
