from django.urls import path
from .views import BookListView, MyBooksView, BorrowBookView, BookCreationView, BorrowListUsersView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('create/', BookCreationView.as_view(), name='create_book'),
    path('my_books/', MyBooksView.as_view(), name='my_books'),
    path('list_borrow/', BorrowListUsersView.as_view(), name='list_borrow'),
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow_book'),
]
