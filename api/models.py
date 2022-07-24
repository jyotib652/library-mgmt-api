from datetime import timedelta, datetime

import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles
    LIBRARIAN = 1
    MEMBER = 2

    ROLE_CHOICES = (
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    # Roles
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="Public Identifier")
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    created_by = models.EmailField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return f"{self.email} ID: {self.id}"


class Book(models.Model):

    # These fields tie to the Book status
    AVAILABLE = 1
    BORROWED = 2

    ROLE_CHOICES = (
        (BORROWED, 'Borrowed'),
        (AVAILABLE, 'Available')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="Public Identifier")
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # isbn = models.PositiveIntegerField()
    # category = models.CharField(max_length=50)
    status = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=1)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ID: {self.id}"


def expiry():
    # return datetime.today() + timedelta(days=14)
    return timezone.now() + timedelta(days=14)



# class IssuedBook(models.Model):

#     AVAILABLE = 1
#     BORROWED = 2

#     ROLE_CHOICES = (
#         (BORROWED, 'Borrowed'),
#         (AVAILABLE, 'Available')
#     )
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
#     status = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
#     issued_date = models.DateTimeField(auto_now=True)
#     expiry_date = models.DateTimeField(default=expiry)

#     def __str__(self):
#         return f"{self.book}--{self.user}"



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

    
