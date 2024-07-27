from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ReaderRegisterForm(UserCreationForm):
    address = forms.CharField(max_length=255)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'address']


class LibrarianRegisterForm(UserCreationForm):
    employee_id = forms.CharField(max_length=10)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'employee_id']
