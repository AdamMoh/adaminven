from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    category = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)