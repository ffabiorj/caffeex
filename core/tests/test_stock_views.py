import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Stock, CoffeeBag
from serializers import StockSerializer, CoffeeBagSerializer
from django.contrib.auth.models import User


class GetAllStocksTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()

        Stock.objects.create(
            name='Coffex', origin_farm='West',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )
        Stock.objects.create(
            name='Hall', origin_farm='North',
            quantity_bags_availible=20,
            stock_capacity=50,
            owner=self.user
        )
        Stock.objects.create(
            name='EUA', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

    def test_get_all_stocks_if_is_super_admin(self):
        # get api response
        self.client.force_login(self.user)
        response = self.client.get(reverse('stocks'))
        # get data from db
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOneStock(TestCase):
    def setUp(self):
        self.useradmin = User.objects.create(username='test', password='12345', is_superuser=True)
        self.user = User.objects.create(username='testuser', password='12345')
        self.user2 = User.objects.create(username='falso', password='12345')

        self.client = Client()

        Stock.objects.create(
            name='Casa', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

        Stock.objects.create(
            name='EUA', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user2
        )

        Stock.objects.create(
            name='FOGO', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.useradmin
        )

    def test_get_stock_by_owner(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('stocks'))

        stocks = Stock.objects.filter(owner=self.user)
        serializer = StockSerializer(stocks, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateStock(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()

        self.valid_payload = {
            'name': 'Fazenda',
            'origin_farm': 'South',
            'quantity_bags_availible': 10,
            'stock_capacity': 30,
            'owner': self.user.id
        }
        self.invalid_payload = {
            'name': 'Fazenda',
            'origin_farm': '',
            'quantity_bags_availible': '',
            'stock_capacity': 30,
            'owner': self.user.id
        }

    def test_create_a_valid_stock(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('stocks'),
        data=json.dumps(self.valid_payload),
        content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateAnStock(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()
        self.client.force_login(self.user)

        self.stock = Stock.objects.create(
            name='Casa', 
            origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

        self.valid_payload = {
            'name': 'Fazenda',
            'origin_farm': 'South',
            'quantity_bags_availible': 10,
            'stock_capacity': 30,
            'owner':self.user.id
        }

        self.invalid_payload = {
            'name': 'Fazenda',
            'origin_farm': '',
            'stock_capacity': 30,
        }
    
    def test_valid_update_stock(self):
        response = self.client.put(
            reverse('stock', kwargs={'pk': self.stock.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_stock(self):
        response = self.client.put(
            reverse('stock', kwargs={'pk': self.stock.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteStockTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()
        self.client.force_login(self.user)

        self.stock = Stock.objects.create(
            name='Casa', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

        self.stock1 = Stock.objects.create(
            name='EUA', origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

    def test_valid_delete_stock(self):
        response = self.client.delete(
            reverse('stock', kwargs={'pk': self.stock.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_stock(self):
        response = self.client.delete(
            reverse('stock', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
