import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.test import TestCase


class GetStatusCodeErrorTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_error_403_try_to_access_stocks(self):
        response = self.client.get(reverse('stocks'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_error_403_try_to_access_coffeebags(self):
        response = self.client.get(reverse('coffeebags'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_error_message_try_to_access_without_login(self):
        response = self.client.get(reverse('coffeebags'))
        error = {
            "detail": "Authentication credentials were not provided."
        }
        self.assertEqual(response.data, error)