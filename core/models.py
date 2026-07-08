from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    WORKER = 'worker'
    REGULAR_USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (WORKER, 'Worker'),
        (REGULAR_USER, 'User'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=REGULAR_USER)
    bio = models.TextField(max_length=150, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
