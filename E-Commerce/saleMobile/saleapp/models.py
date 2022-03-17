from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='Avatars/%Y/%m')


class Category(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    mail = models.EmailField(null=True)


class Product(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to='Products/%Y/%m')
    price = models.DecimalField(decimal_places=3, max_digits=12)
    manufacturer = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.SET_NULL,
                                 null=True)


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    monitor = models.TextField(max_length=255, null=True, blank=True)
    processors = models.TextField(max_length=255, null=True, blank=True)
    RAM = models.IntegerField()
    battery = models.IntegerField()


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
