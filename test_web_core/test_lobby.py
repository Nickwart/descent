from rest_framework.test import APIRequestFactory
from lobby.views import LobbyUserViews, LobbyView, LobbyListCreateView, LobbyUserListCreateView
from django.test import TestCase
from django.contrib.auth.models import User
from lobby.models import Lobby, LobbyUser
import django.test


class LobbyUserTestCase(TestCase):
    def setUp(self):

        self.factory = APIRequestFactory()
        self.client = django.test.Client()
        self.test_user = User.objects.create_user(username='test_user', email='qqq@gmail.com', password='bananana')
        self.lobby = Lobby.objects.create(
                name='lobby_for_tests',
                private=True, password='bananana',
                creator_id=self.test_user.id
        )

    def test_user_joined_lobby(self):
        auth = self.client.post(f"/login/", data={"username": "test_user", "password": "bananana"})
        headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
        request = self.factory.post('/lobby_user/', {"lobby_id": str(self.lobby.id)}, format='json', **headers)
        response = LobbyUserViews.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_not_logged_in_user_fails(self):
        request = self.client.post("/lobby_user/", {"lobby_id": self.lobby.id})
        self.assertEqual(request.status_code, 403)

    def test_max_users_count(self):
        test_user2 = User.objects.create_user(username='test_user2', email='qqq2@gmail.com', password='bananana')
        test_user3 = User.objects.create_user(username='test_user3', email='qqq3@gmail.com', password='bananana')
        test_user4 = User.objects.create_user(username='test_user4', email='qqq4@gmail.com', password='bananana')
        test_user5 = User.objects.create_user(username='test_user5', email='qqq5@gmail.com', password='bananana')
        test_user6 = User.objects.create_user(username='test_user6', email='qqq6@gmail.com', password='bananana')
        test_user7 = User.objects.create_user(username='test_user7', email='qqq7@gmail.com', password='bananana')

        users = [self.test_user, test_user2, test_user3, test_user4, test_user5, test_user6, test_user7]

        user_counter = 0
        for user in users:
            auth = self.client.post(f"/login/", data={"username": user.username, "password": "bananana"})
            headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
            request = self.factory.post('/lobby_user/', {"lobby_id": str(self.lobby.id)}, format='json', **headers)
            response = LobbyUserViews.as_view()(request)
            user_counter += 1
            if user_counter <= 5:
                self.assertEqual(response.status_code, 200)
            elif user_counter > 5:
                self.assertEqual(response.status_code, 403)

    def test_lobby_user_deletes(self):
        auth = self.client.post(f"/login/", data={"username": "test_user", "password": "bananana"})
        headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
        request1 = self.factory.post('/lobby_user/', {"lobby_id": str(self.lobby.id)}, format='json', **headers)
        response1 = LobbyUserViews.as_view()(request1)
        request = self.factory.delete(f"/lobby_user/<uuid:lobby>/", **headers)

        self.assertEqual(LobbyUser.objects.filter(lobby_id=self.lobby.id, user_id=self.test_user.id).count(), 1)
        response = LobbyUserListCreateView.as_view()(request, lobby=self.lobby.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(LobbyUser.objects.filter(lobby_id=self.lobby.id, user_id=self.test_user.id).count(), 0)


class LobbyTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = django.test.Client()
        self.test_user = User.objects.create_user(username='test_user', email='qqq@gmail.com', password='bananana')

    def test_lobby_creates(self):
        auth = self.client.post(f"/login/", data={"username": "test_user", "password": "bananana"})
        headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
        request = self.factory.post("/lobby/", {
            "name": "test_lobby_name",
            "private": False,
            "password": "bananana"}, format="json", **headers)

        response = LobbyView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_lobby_deletes(self):
        lobby = Lobby.objects.create(
            name='lobby_for_tests',
            private=True, password='bananana',
            creator_id=self.test_user.id
        )
        auth = self.client.post(f"/login/", data={"username": "test_user", "password": "bananana"})
        headers = {"HTTP_Authorization": f"Bearer {auth.json()['access']}"}
        request = self.factory.delete(f"/lobby/<uuid:lobby>/", **headers)

        self.assertEqual(Lobby.objects.filter(id=lobby.id).count(), 1)
        response = LobbyListCreateView.as_view()(request, lobby=lobby.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Lobby.objects.filter(id=lobby.id).count(), 0)
