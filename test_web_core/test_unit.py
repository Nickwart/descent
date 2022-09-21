from rest_framework.test import APIRequestFactory
from unit.views import UnitCreateView, UnitListCreateView
from django.test import TestCase
from django.contrib.auth.models import User
from unit.models.unit_model import Unit
import django.test
import json


class HeroTestCase(TestCase):
    def setUp(self):

        self.factory = APIRequestFactory()
        self.client = django.test.Client()
        self.test_user = User.objects.create_user(username='test_user', email='qqq@gmail.com', password='bananana')

    def test_unit_creates(self):
        auth = self.client.post(f"/login/", data={"username": "test_user", "password": "bananana"})
        headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
        request = self.factory.post('/unit/',
                                    {"hero_name": "SINDRAEL", "hero_class": "BERSERKER"},
                                    format='json', **headers)
        response = UnitCreateView.as_view()(request)
        self.assertEqual(response.status_code, 204)
