from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


# Define a custom user manager to handle user creation
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Define the custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# Define a model for Topics in order to categorize lessons
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Define a model for Lessons
class Lessons(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


# Define a model for Classes
class Classes(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='classes')
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    booked = models.BooleanField(default=False)
    phone = PhoneNumberField(null=True)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=30, null=True)

    class Meta:
        # Define the default ordering for classes in order to find easier Classes connected with lesson
        ordering = ["start_time", "pk"]