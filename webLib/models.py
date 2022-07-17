from django.db import models
import uuid
from django.core import validators
from django.contrib.auth.models import User

class Author(models.Model):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']
        unique_together = ('name', 'age')

    TYPES = {
        ('a', 'foreign'),
        ('b', 'donestic'),
        ('c', 'other')
    }

    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(
        verbose_name='Имя автора', 
        max_length=200, 
        validators=[validators.RegexValidator(
            regex='^.* $', 
            message='Романс')])
    age = models.PositiveIntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name="Почта")
    ltrType = models.CharField(max_length=1 ,verbose_name='Тип литературы', 
                                choices=TYPES, default='a')

    def info(self):
        name = "Имя: %s" % self.name
        age = "Возраст: %s" % self.age
        email = "Почта: %s" % self.email
        ltrType = "Тип: %s" % self.get_ltrType_display()
        return [name, age, email, ltrType]

    def __str__(self) :
        return self.name

class Book(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        get_latest_by = 'piblished'

    title = models.CharField(max_length=200)
    description = models.TextField()
    page_num = models.PositiveIntegerField()
    piblished = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ExtUser(models.Model):

    desc = models.CharField(max_length=200)
    is_logged = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.desc

class Product(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Store(models.Model):

    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='Stores')

    def __str__(self):
        return self.name

