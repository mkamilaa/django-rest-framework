from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author,related_name = 'books', on_delete=models.CASCADE)
