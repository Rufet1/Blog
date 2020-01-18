from django import forms
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    sentemail = forms.CharField(max_length=8)

class ForgetForm(forms.Form):
    input = forms.CharField(max_length=255,label='İstifadəçi adı və ya email ünvanınızı daxil edin')

    # def clean_input(self):
    #     all_emails = []
    #     all_users = []
    #     all_user = User.objects.all()
    #     input = self.cleaned_data.get('input')
    #     for i in all_user:
    #         all_emails.append(i.email)
    #     for i in all_user:
    #         all_users.append(i.username)
    #     if input and not input in all_emails:
    #         raise forms.ValidationError('movcud deyil')
    #         return input
    #     return super(ForgetForm, self).clean()