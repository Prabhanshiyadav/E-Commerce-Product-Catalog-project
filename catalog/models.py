from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
