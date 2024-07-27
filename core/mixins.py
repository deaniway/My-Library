from django.utils import timezone
from django.contrib import messages
from apps.books.models import Book
from django.shortcuts import redirect


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
