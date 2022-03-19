from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/%Y/%m', default=None)


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    mail = models.EmailField(null=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m', default=None)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    manufacturer = models.CharField(max_length=50, null=False)
    description = RichTextField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='products',
                                 related_query_name='my_product',
                                 null=True)

    def __str__(self):
        return self.name


class StatusOrder(models.Model):
    status = models.CharField(max_length=50, null=False, unique=True)


class Order(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=3, max_digits=10)
    destination = models.CharField(max_length=255, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusOrder, on_delete=models.SET_NULL, null=True)


class OrderDetail(models.Model):
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=3, max_digits=10)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
