from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    category = models.TextField()
    description = models.TextField()