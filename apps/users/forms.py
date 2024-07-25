from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Reader


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ReaderRegisterForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'address']
