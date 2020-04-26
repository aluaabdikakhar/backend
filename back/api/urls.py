from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views_cbv import BookDetailAPIView, RegistrationAPIView, MyBooksAPIView, MyBooksView
from .views_fbv import category_books, categories, books

urlpatterns = [
    path('categories/', categories),
    path('categories/<int:id>/', category_books),
    path('books/', books),
    path('books/<int:isbn>/', BookDetailAPIView.as_view()),
    path('login/', obtain_jwt_token),
    path('registration/', RegistrationAPIView.as_view()),
    path('users/<str:name>/mybooks/', MyBooksAPIView.as_view()),

    path('users/<str:name>/mybooks/<int:id>/', MyBooksView.as_view()),
]