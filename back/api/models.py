from django.db import models

class ManagerPublisher(models.Manager):
    def get_queryset(self):
        return super(ManagerPublisher, self).get_queryset().filter(year__lte=2020)

class Category(models.Model):
    title = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }

class Book(models.Model):
    isbn = models.IntegerField(null=True)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=2000000)
    image = models.TextField(max_length=1000)
    publisher = models.TextField(max_length=100)
    author = models.TextField(max_length=200)
    genre = models.TextField(max_length=100)
    year = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    book = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    objects = models.Manager()
    manager = ManagerPublisher()

    def to_json(self):
        return{
            'id': self.id,
            'isbn': self.isbn,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'publisher': self.publisher,
            'author': self.author,
            'genre': self.genre,
            'year': self.year,
            'pages': self.pages,
            'book': self.book,
        }

class MyBooks(models.Model):
    books = models.ManyToManyField('Book', related_name='books')

class User(models.Model):
    mail = models.TextField(max_length=50)
    password = models.TextField(max_length=100)
    books = models.OneToOneField(MyBooks, on_delete=models.PROTECT, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'mail': self.mail,
            'password': self.password
        }