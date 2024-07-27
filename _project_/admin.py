from django.contrib import admin
from apps.books.models import Book
from apps.users.models import Librarian, Reader
from simple_history.admin import SimpleHistoryAdmin


class BookAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'genre', 'is_borrowed')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('is_borrowed',)


class LibrarianAdmin(SimpleHistoryAdmin):
    list_display = ('user', 'employee_id',)
    search_fields = ('user__last_name', 'employee_id')
    list_filter = ('employee_id',)


class ReaderAdmin(SimpleHistoryAdmin):
    list_display = ('user','get_full_name', 'address')
    search_fields = ('user__first_name', 'user__last_name', 'address')
    list_filter = ('user', 'user__last_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Librarian, LibrarianAdmin)
admin.site.register(Reader, ReaderAdmin)
