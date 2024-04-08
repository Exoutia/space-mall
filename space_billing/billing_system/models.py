from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2)


class BillProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='products')
