from django import forms
class ConnectForm(forms.Form):
    login = forms.CharField(max_length=30)
    m_pass = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

from .models import *
class CreerContactsForm(forms.ModelForm):
    class Meta:
         model = Contacts
         fields = '__all__'
