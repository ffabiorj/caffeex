from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Stock, CoffeeBag


class CoffeeBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeBag
        exclude = ['stock', 'created']


class StockSerializer(serializers.ModelSerializer):
    space_availible = serializers.ReadOnlyField()
    coffees_types = CoffeeBagSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        exclude = ['owner']
