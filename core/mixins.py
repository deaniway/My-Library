from django.contrib.auth import login
from django.utils import timezone
from django.contrib import messages
from apps.books.models import Book
from apps.users.forms import ReaderRegisterForm, LibrarianRegisterForm
from django.shortcuts import redirect


class LibrarianFormMixin:
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['librarian_form'] = LibrarianRegisterForm(self.request.POST)
        else:
            data['librarian_form'] = LibrarianRegisterForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        reader_form = context['librarian_form']
        if reader_form.is_valid():
            response = super().form_valid(form)
            self.object.is_librarian = True
            self.object.save()
            reader = reader_form.save(commit=False)
            reader.user = self.object
            reader.save()
            login(self.request, self.object)
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ReaderFormMixin:
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['reader_form'] = ReaderRegisterForm(self.request.POST)
        else:
            data['reader_form'] = ReaderRegisterForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        reader_form = context['reader_form']
        if reader_form.is_valid():
            response = super().form_valid(form)
            self.object.is_reader = True
            self.object.save()
            reader = reader_form.save(commit=False)
            reader.user = self.object
            reader.save()
            login(self.request, self.object)
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))


class BorrowListMixin:
    def get_queryset(self):
        return Book.objects.filter(is_borrowed=True).select_related('borrowed_by')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = timezone.now()
        for book in context['list_borrow']:
            book.borrowed_duration = current_time - book.borrowed_date

            days = book.borrowed_duration.days
            hours, remainder = divmod(book.borrowed_duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            book.borrowed_duration = '{:d} дн {:02} ч {:02} мин'.format(days, hours, minutes)
        return context


class UserIsLibrarianRequiredMixin:
    def test_func(self):
        return self.request.user.is_librarian

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для добавления книг.')
        return redirect('list')
