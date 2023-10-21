from rest_framework.test import APIClient
from django.test import TestCase


class MyTestCase(TestCase):
    def test_1_plus_1(self):
        client = APIClient()
        response = client.get('/api/v1/posts/')
        assert response.status_code == 200
