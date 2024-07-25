from django.contrib import admin
from django.urls import path, include

from _project_.views import UserLoginView, UserLogoutView, IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', include('apps.users.urls')),
    path('books/', include('apps.books.urls')),
]
