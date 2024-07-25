from django.contrib import admin
from apps.books.models import Book
from apps.users.models import User, Librarian, Reader

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Librarian)
admin.site.register(Reader)
