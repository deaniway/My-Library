from django.contrib import admin
from apps.books.models import Book
from apps.users.models import User, Librarian, Reader
from simple_history.admin import SimpleHistoryAdmin


class BookAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'genre', 'is_borrowed')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('is_borrowed',)


class UserAdmin(SimpleHistoryAdmin):
    list_display = ('username', 'is_librarian', 'is_reader')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_librarian', 'is_reader')


class LibrarianAdmin(SimpleHistoryAdmin):
    list_display = ('user', 'employee_id',)
    search_fields = ('user', 'employee_id')
    list_filter = ('employee_id',)


class ReaderAdmin(SimpleHistoryAdmin):
    list_display = ('first_name', 'last_name', 'address')
    search_fields = ('first_name', 'last_name', 'address')
    list_filter = ('user',)


admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Librarian, LibrarianAdmin)
admin.site.register(Reader, ReaderAdmin)
