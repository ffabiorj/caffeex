import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Stock, CoffeeBag
from serializers import CoffeeBagSerializer
from django.contrib.auth.models import User


class GetAllCoffeebagsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()

        self.stock = Stock.objects.create(
            name='Coffex',
            origin_farm='West',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )
        CoffeeBag.objects.create(
            coffee_type='Black',
            origin='South',
            expirate_date='2020-12-12',
            quantity_bags=20,
            stock=self.stock
        )
        CoffeeBag.objects.create(
            coffee_type='Blue',
            origin='North',
            expirate_date='2020-12-12',
            quantity_bags=25,
            stock=self.stock
        )

    def test_get_all_coffees_bags_if_is_super_admin(self):
        # get api response
        self.client.force_login(self.user)
        response = self.client.get(reverse('coffeebags'))
        # get data from db
        coffeebags = CoffeeBag.objects.all()
        serializer = CoffeeBagSerializer(coffeebags, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOneCoffeebag(TestCase):
    def setUp(self):
        self.useradmin = User.objects.create(username='test', password='12345', is_superuser=True)
        self.user = User.objects.create(username='testuser', password='12345')

        self.client = Client()

        self.stock = Stock.objects.create(
            name='Casa',
            origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

        self.stock1 = Stock.objects.create(
            name='FOGO',
            origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.useradmin
        )

        CoffeeBag.objects.create(
            coffee_type='Black',
            origin='South',
            expirate_date='2020-12-12',
            quantity_bags=20,
            stock=self.stock
        )
        CoffeeBag.objects.create(
            coffee_type='Blue',
            origin='North',
            expirate_date='2020-12-12',
            quantity_bags=25,
            stock=self.stock
        )

    def test_get_coffeebags_by_owner(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('coffeebags'))

        coffeebags = CoffeeBag.objects.filter(stock=self.user.id)
        serializer = CoffeeBagSerializer(coffeebags, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateCoffeeBag(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', is_superuser=True)
        self.client = Client()

        self.stock = Stock.objects.create(
            name='Casa',
            origin_farm='North',
            quantity_bags_availible=30,
            stock_capacity=50,
            owner=self.user
        )

        self.valid_payload = {
            "coffee_type": "Blue",
            "origin": "North",
            "expirate_date": "2020-12-12",
            "quantity_bags": 25,
            "stock": self.stock.id
        }
        self.invalid_payload = {
            "coffee_type": "Blue",
            "origin": "North",
            "expirate_date": "2020-12-12",
            "quantity_bags": 25,
        }

    def test_create_a_valid_stock(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('coffeebags'),
                                    data=json.dumps(self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_invalid_coffeebags(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('coffeebags'),
                                    data=json.dumps(self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateAnStock(TestCase):
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

        self.coffebag = CoffeeBag.objects.create(
            coffee_type='Black',
            origin='South',
            expirate_date='2020-12-12',
            quantity_bags=20,
            stock=self.stock
        )

        self.valid_payload = {
            "coffee_type": "Blue",
            "origin": "North",
            "expirate_date": "2020-05-12",
            "quantity_bags": 25,
            "stock": self.stock.id
        }

        self.invalid_payload = {
            "coffee_type": "Blue",
            "origin": "North",
            "expirate_date": "2020-05-12",
        }

    def test_valid_update_coffeebag(self):
        response = self.client.put(
            reverse('coffeebag', kwargs={'pk': self.coffebag.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_coffeebag(self):
        response = self.client.put(
            reverse('coffeebag', kwargs={'pk': self.stock.pk}),
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

        self.coffeebag = CoffeeBag.objects.create(
            coffee_type='Blue',
            origin='North',
            expirate_date='2020-12-12',
            quantity_bags=25,
            stock=self.stock
        )

    def test_valid_delete_coffeebag(self):
        response = self.client.delete(
            reverse('coffeebag', kwargs={'pk': self.coffeebag.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_coffeebag(self):
        response = self.client.delete(
            reverse('coffeebag', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
