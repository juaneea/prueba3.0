from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuario.models import User


class InicioSesionForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
