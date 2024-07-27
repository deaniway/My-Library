from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from .models import Book
from .forms import BookCreationForm
from .mixins import BorrowListMixin
from apps.users.models import Reader


class BookCreationView(CreateView):
    model = Book
    form_class = BookCreationForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('list')


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    ordering = ['title']


class BorrowListUsersView(BorrowListMixin, ListView):
    model = Book
    template_name = 'books/list_borrow.html'
    context_object_name = 'list_borrow'
    ordering = ['borrowed_by']


class MyBooksView(TemplateView):
    template_name = 'books/my_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            reader = Reader.objects.get(user=self.request.user)
            context['borrowed_books'] = reader.borrowed_books.all().order_by('title')
        except Reader.DoesNotExist:
            context['borrowed_books'] = None
        return context


class BorrowBookView(View):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs['book_id'])

        if book.is_borrowed:
            if book.borrowed_by == Reader.objects.get(user=request.user):
                book.is_borrowed = False
                book.borrowed_by = None
                book.borrowed_date = None
                messages.info(request, f'Вы успешно вернули книгу "{book.title}".')

        else:
            book.is_borrowed = True
            book.borrowed_by = Reader.objects.get(user=request.user)
            book.borrowed_date = timezone.now()
            messages.success(request, f'Вы успешно взяли книгу "{book.title}".')

        book.save()
        return redirect('list')
