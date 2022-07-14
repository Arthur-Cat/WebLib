from pyexpat import model
from django.db import models

class Product(models.Model):

    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    isActive = models.BooleanField(verbose_name='Active', default=True, null=True)

    def __str__(self):
        return self.title


class Bin(models.Model):

    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class Home(models.Model):

    size = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="The size", null=True)
    cost = models.IntegerField(verbose_name='Price', null=True)
    adr = models.CharField(max_length=200, verbose_name='Addres', default='Armavits Str')
    bol = models.BooleanField(verbose_name="balcony", default=True)

    def __str__(self):
        return self.adr