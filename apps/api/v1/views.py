from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.books.models import Book
from .serializers import BookSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BorrowBookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.is_borrowed:
            return Response({"error": "Книга уже на руках"}, status=status.HTTP_400_BAD_REQUEST)

        if not request.user.is_authenticated:
            return Response({"error": "Необходимо войти в систему для взятия книги"},
                            status=status.HTTP_401_UNAUTHORIZED)

        book.is_borrowed = True
        book.borrowed_by = request.user
        book.borrowed_date = timezone.now()
        book.save()
        return Response(BookSerializer(book).data)


class ReturnBookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if not request.user.is_authenticated:
            return Response({"error": "Необходимо войти в систему для возврата книги"},
                            status=status.HTTP_401_UNAUTHORIZED)

        if not book.is_borrowed or book.borrowed_by != request.user:
            return Response({"error": "Эта книга не была взята вами"}, status=status.HTTP_400_BAD_REQUEST)

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None
        book.save()
        return Response(BookSerializer(book).data)


class BorrowedBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Book.objects.none()
        return Book.objects.filter(borrowed_by=self.request.user, is_borrowed=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not request.user.is_authenticated:
            return Response({"error": "Необходимо войти в систему для просмотра взятых книг"},
                            status=status.HTTP_401_UNAUTHORIZED)

        response_data = []
        for book in queryset:
            borrowed_days = (timezone.now() - book.borrowed_date).days
            response_data.append({
                'title': book.title,
                'borrowed_date': book.borrowed_date,
                'borrowed_days': borrowed_days
            })
        return Response(response_data)
