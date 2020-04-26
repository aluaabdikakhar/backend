from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Book, User, MyBooks
from .serializers import CategorySerializer, UserSerializer, BookSerializer, MyBooksSerializer

class BookDetailAPIView(APIView):
    def get_object(self, isbn):
        try:
            return Book.objects.get(isbn=isbn)
        except Book.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, isbn):
        book = self.get_object(isbn)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, isbn):
        book = self.get_object(isbn)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, isbn):
        book = self.get_object(isbn)
        book.delete()
        return Response({'deleted': True})

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

class MyBooksAPIView(APIView):
    def get_object(self, name):
        try:
            return User.objects.get(mail=name).books
        except User.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, name):
        books = self.get_object(name)
        serializer = MyBooksSerializer(books)
        return Response(serializer.data)


class MyBooksView(APIView):
    def get_object(self, name, id):
        try:
            return User.objects.get(mail=name)
        except User.DoesNotExist as e:
            return Response({'error': str(e)})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, isbn):
        book = self.get_object(isbn)
        book.delete()
        return Response({'deleted': True})