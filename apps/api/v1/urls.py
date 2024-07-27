from django.urls import path
from .views import BookListView, BookDetailView, BorrowBookView, ReturnBookView, BorrowedBooksView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('books/<int:pk>/return/', ReturnBookView.as_view(), name='return-book'),
    path('books/borrowed/', BorrowedBooksView.as_view(), name='borrowed-books'),
]
