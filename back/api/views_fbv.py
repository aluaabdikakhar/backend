from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Book, User
from .serializers import CategorySerializer, UserSerializer, BookSerializer

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def category_books(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        books = Book.objects.filter(category=category)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

