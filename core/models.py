from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    name = models.CharField('Name stock', max_length=100, blank=False)
    origin_farm = models.CharField('Origin farm', max_length=100)
    quantity_bags_availible = models.IntegerField(blank=True, null=True)
    stock_capacity = models.IntegerField(blank=False, null=False)
    owner = models.ForeignKey(User, related_name='stock', on_delete=models.CASCADE)

    def space_availible(self):
        return self.stock_capacity - self.quantity_bags_availible

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class CoffeeBag(models.Model):
    coffee_type = models.CharField('Coffee type', max_length=50)
    origin = models.CharField('Origin', max_length=100)
    expirate_date = models.DateField()
    quantity_bags = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    stock = models.ForeignKey(Stock, related_name='coffees_types', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.coffee_type
