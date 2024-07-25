from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.mixins import ReaderFormMixin, LibrarianFormMixin
from .models import User
from .forms import UserRegisterForm


class UserReaderCreateView(ReaderFormMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('index')


class UserLibrarianCreateView(LibrarianFormMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/creation_librarian.html'
    success_url = reverse_lazy('index')
