from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Reader, Librarian
from .forms import ReaderRegisterForm, LibrarianRegisterForm


class UserReaderCreateView(CreateView):
    model = Reader
    form_class = ReaderRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        Reader.objects.create(
            user=self.object,
            address=form.cleaned_data['address']
        )
        login(self.request, self.object)
        return response


class UserLibrarianCreateView(CreateView):
    model = Librarian
    form_class = LibrarianRegisterForm
    template_name = 'users/creation_librarian.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        Librarian.objects.create(
            user=self.object,
            employee_id=form.cleaned_data['employee_id']
        )
        login(self.request, self.object)
        return response
