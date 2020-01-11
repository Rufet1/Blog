from django import forms


class EmailForm(forms.Form):
    sentemail = forms.CharField(max_length=8)