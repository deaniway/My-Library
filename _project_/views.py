from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('list')

    def form_valid(self, form):
        messages.success(self.request, _("Вход выполнен!"))
        return super().form_valid(form)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = _("Вы успешно вышли из системы")

    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
