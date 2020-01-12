from django import forms


class EmailForm(forms.Form):
    sentemail = forms.CharField(max_length=8)

class ForgetForm(forms.Form):
    input = forms.CharField(max_length=255,label='İstifadəçi adı və ya email ünvanınızı daxil edin')