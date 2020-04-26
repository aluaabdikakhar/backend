from rest_framework import serializers
from .models import User, Category, Book, MyBooks
from django.contrib.auth import get_user_model
UserModel = get_user_model()
JSON_ALLOWED_OBJECTS = (dict,list,tuple,str,int,bool)

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ('id', 'title', 'books')

    def create(self, validated_data):
        category = Category.objects.create(title=validated_data.get('title'))
        return category

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'description', 'image', 'publisher', 'author', 'genre', 'year', 'pages', 'book', 'category_id', 'category')

class MyBooksSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True,)

    class Meta:
        model = MyBooks
        fields = ("__all__")

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mail = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, write_only=True)
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User, UserModel
        fields = ('id', 'mail', 'password', 'books')

    def create(self, validated_data):
        user2 = UserModel.objects.create_user(
            username=validated_data['mail'],
            password=validated_data['password']
        )
        user = User.objects.create(
            mail=validated_data.get('mail'),
            password=validated_data.get('password'),
            books=MyBooks.objects.create()
        )
        return user
