from rest_framework import serializers
from core.models import Stock, CoffeeBag


class CoffeeBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoffeeBag
        exclude = ['created']


class StockSerializer(serializers.ModelSerializer):
    space_availible = serializers.ReadOnlyField()
    coffees_types = CoffeeBagSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'
