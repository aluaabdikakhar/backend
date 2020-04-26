from django.contrib import admin
from .models import Book, User, Category

admin.register(User),
admin.register(Book),
admin.register(Category)