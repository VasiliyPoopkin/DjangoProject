from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .pagination import UserLimitPagination, OtherLimitPagination
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend




#task 1

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),  # Включіть роутери для кожного додатку
    # ...
]

#task 2

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
}
# update settings.py

#task 3

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserLimitPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = OtherLimitPagination

class UserLimitPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

class OtherLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5

#task 4

INSTALLED_APPS = [
    'django_filters',
]
# update settings.py

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['User'] #Book, Purchase
