import os
from dotenv import load_dotenv
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.http import HttpResponse
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


#task 1

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False  #DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

#task 2


class ApplicationUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Необхідно вказати email користувача")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ApplicationUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


#task 3


def users_view(request):
    return HttpResponse("Hello, users!")


urlpatterns = [
    path('users/', views.users_view, name='users_view'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),
]

