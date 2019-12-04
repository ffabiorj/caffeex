from django.test import TestCase
from core.models import Stock, CoffeeBag
from django.contrib.auth.models import User


class StockTest(TestCase):
    """ Test module for Stock model."""

    def setUp(self):
        user = User.objects.create(username='testuser', password='12345')
        Stock.objects.create(
            name='Coffex', origin_farm='West',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=user
        )
        Stock.objects.create(
            name='Hall', origin_farm='North',
            quantity_bags_availible=20,
            stock_capacity=10,
            owner=user
        )

    def test_name_stock(self):
        coffex = Stock.objects.get(name='Coffex')
        Hall = Stock.objects.get(name='Hall')

        self.assertEqual(coffex.name, 'Coffex')
        self.assertEqual(Hall.name, 'Hall')


class CoffeeBagTest(TestCase):
    """ Test module for CoffeeBag model."""

    def setUp(self):
        user = User.objects.create(username='testuser', password='12345')
        self.stock = Stock.objects.create(
            name='Coffex', origin_farm='West',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=user
        )
        CoffeeBag.objects.create(
            coffee_type='Black',
            origin='West',
            expirate_date='2020-12-12',
            quantity_bags=20,
            stock=self.stock
        )
        CoffeeBag.objects.create(
            coffee_type='Blue',
            origin='South',
            expirate_date='2020-12-12',
            quantity_bags=20,
            stock=self.stock
        )

    def test_type_coffee(self):
        black = CoffeeBag.objects.get(coffee_type='Black')
        blue = CoffeeBag.objects.get(coffee_type='Blue')

        self.assertEqual(black.coffee_type, 'Black')
        self.assertEqual(blue.coffee_type, 'Blue')
