from rest_framework import serializers
from apps.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'is_borrowed', 'borrowed_by', 'borrowed_date']
