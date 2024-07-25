from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.mixins import UserFormMixin
from .models import User
from .forms import UserRegisterForm


class UserCreateView(UserFormMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('index')
