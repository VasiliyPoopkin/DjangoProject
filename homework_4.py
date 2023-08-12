from .models import User
from .models import Book
from django.views import View
from .models import Purchase
from .views import UserListView, UserDetailView
from .views import BookListView, BookDetailView
from .views import PurchaseListView, PurchaseDetailView
from django import forms
from django.shortcuts import render, redirect
from .forms import UserForm
from .forms import BookForm
from .forms import PurchaseForm
from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView
from .views import BookListView, BookDetailView, BookCreateView

#task 1

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/user_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'user/user_detail.html', {'user': user})

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        return render(request, 'book/book_detail.html', {'book': book})

class PurchaseListView(View):
    def get(self, request):
        purchases = Purchase.objects.all()
        return render(request, 'purchase/purchase_list.html', {'purchases': purchases})

class PurchaseDetailView(View):
    def get(self, request, id):
        purchase = Purchase.objects.get(pk=id)
        return render(request, 'purchase/purchase_detail.html', {'purchase': purchase})


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
]

urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase-detail'),
]

#task 2


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['user', 'book', 'purchase_date']

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user/user_create.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
        return render(request, 'user/user_create.html', {'form': form})

class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book/book_create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, 'book/book_create.html', {'form': form})

class PurchaseCreateView(View):
    def get(self, request):
        form = PurchaseForm()
        return render(request, 'purchase/purchase_create.html', {'form': form})

    def post(self, request):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase-list')
        return render(request, 'purchase/purchase_create.html', {'form': form})


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
]

urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),
]

