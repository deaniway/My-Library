from django.views.generic import ListView, TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from .models import Book
from .forms import BookCreationForm


class BookCreationView(CreateView):
    model = Book
    form_class = BookCreationForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('list')

    def test_func(self):
        return self.request.user.is_librarian

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для добавления книг.')
        return redirect('list')


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    ordering = ['title']


class BorrowListUsersView(ListView):
    model = Book
    template_name = 'books/list_borrow.html'
    context_object_name = 'list_borrow'
    ordering = ['borrowed_by']

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


class MyBooksView(TemplateView):
    template_name = 'books/my_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrowed_books'] = self.request.user.borrowed_books.all().order_by('title')
        return context


class BorrowBookView(View):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs['book_id'])

        if book.is_borrowed:
            if book.borrowed_by == request.user:
                book.is_borrowed = False
                book.borrowed_by = None
                book.borrowed_date = None
                messages.info(request, f'Вы успешно вернули книгу "{book.title}".')

            else:
                messages.error(request, f'Книга "{book.title}" уже взята другим пользователем.', extra_tags='danger')

        else:
            book.is_borrowed = True
            book.borrowed_by = request.user
            book.borrowed_date = timezone.now()
            messages.success(request, f'Вы успешно взяли книгу "{book.title}".')

        book.save()
        return redirect('list')
