from django.db import models
from user.models import User
from book.models import Book
from django.http import JsonResponse
from .models import Book
from .models import Purchase
from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path, include

#task 1

INSTALLED_APPS = [
    'user',
    'book',
    'purchase',
]


#task 2


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} purchased {self.book}"


#task 3


def get_all_books(request):
    books = Book.objects.all()
    data = [{'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date} for book in books]
    return JsonResponse(data, safe=False)


def get_all_purchases(request):
    purchases = Purchase.objects.all()
    data = [{'id': purchase.id, 'user': purchase.user.id, 'book': purchase.book.id, 'purchase_date': purchase.purchase_date} for purchase in purchases]
    return JsonResponse(data, safe=False)


urlpatterns = [
    path('users/', views.get_all_users, name='get_all_users'),
]

urlpatterns = [
    path('books/', views.get_all_books, name='get_all_books'),
]

urlpatterns = [
    path('purchases/', views.get_all_purchases, name='get_all_purchases'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('book.urls')),
    path('', include('purchase.urls')),
]


#task 4


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.user} purchased {self.book}"