from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username




