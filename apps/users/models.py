from django.contrib.auth import get_user_model
from django.db import models


class Reader(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Librarian(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


def get_full_name(self):
    return f'{self.user.first_name} {self.user.last_name}'
