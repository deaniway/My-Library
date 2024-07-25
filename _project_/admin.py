from django.contrib import admin
from apps.books.models import Book
from apps.users.models import User, Librarian, Reader
from simple_history.admin import SimpleHistoryAdmin


class BookAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'author', 'genre', 'is_borrowed')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('is_borrowed',)


admin.site.register(Book, BookAdmin)
admin.site.register(User)
admin.site.register(Librarian)
admin.site.register(Reader)
