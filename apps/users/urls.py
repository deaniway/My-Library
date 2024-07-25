from django.urls import path
from .views import UserReaderCreateView, UserLibrarianCreateView

urlpatterns = [
    path('create_reader/', UserReaderCreateView.as_view(), name='create_reader'),
    path('create_librarian/', UserLibrarianCreateView.as_view(), name='create_librarian'),

]
