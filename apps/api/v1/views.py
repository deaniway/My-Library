from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.books.models import Book
from apps.users.models import Reader
from .serializers import BookSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.is_borrowed:
            return Response({"error": "Книга уже на руках"}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем Reader для текущего пользователя
        reader = get_object_or_404(Reader, user=request.user)

        book.is_borrowed = True
        book.borrowed_by = reader
        book.borrowed_date = timezone.now()
        book.save()

        return Response(BookSerializer(book).data)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        # Получаем Reader для текущего пользователя
        reader = get_object_or_404(Reader, user=request.user)

        if not book.is_borrowed or book.borrowed_by != reader:
            return Response({"error": "Эта книга не была взята вами"}, status=status.HTTP_400_BAD_REQUEST)

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None
        book.save()

        return Response(BookSerializer(book).data)


class BorrowedBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        reader = get_object_or_404(Reader, user=self.request.user)
        return Book.objects.filter(borrowed_by=reader, is_borrowed=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        response_data = []
        for book in queryset:
            borrowed_days = (timezone.now() - book.borrowed_date).days
            response_data.append({
                'title': book.title,
                'borrowed_date': book.borrowed_date,
                'borrowed_days': borrowed_days
            })
        return Response(response_data)
