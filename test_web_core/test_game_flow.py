from game.views import GameCreateAPIView, GameAPIView, MapCreateAPIView, MapTemplateAPIView, MapAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIRequestFactory
from lobby.views import LobbyView, LobbyUserViews
from django.contrib.auth.models import User
from django.test import TestCase
import json


class GameFlowTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = User.objects.create_user(
            username='test_user',
            email='qqq@gmail.com',
            password='bananana'
        )
        self.test_user_1 = User.objects.create_user(
            username='test_user_1',
            email='qqq@gmail.com',
            password='bananana'
        )

    @property
    def bearer_token(self):
        refresh = RefreshToken.for_user(self.test_user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    @property
    def bearer_token_user_1(self):
        refresh = RefreshToken.for_user(self.test_user_1)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_game_flow(self):
        request_create_lobby = self.factory.post("/lobby/", {
            "name": "test_lobby_name",
            "private": False,
            "password": "bananana"}, format="json", **self.bearer_token)

        response_create_lobby = LobbyView.as_view()(request_create_lobby)
        create_lobby_response = json.loads(json.loads(response_create_lobby.content))
        self.assertEqual(response_create_lobby.status_code, 201)

        request_join_lobby = self.factory.post(
            '/lobby_user/',
            {"lobby_id": create_lobby_response['id']},
            format='json',
            **self.bearer_token_user_1)
        response_join_lobby = LobbyUserViews.as_view()(request_join_lobby)
        self.assertEqual(response_join_lobby.status_code, 200)

        request_get_map_template = self.factory.get('/map_template/', **self.bearer_token)
        response_get_map_template = MapTemplateAPIView.as_view()(request_get_map_template, pk=1)
        get_map_template_response = response_get_map_template.data
        self.assertEqual(response_get_map_template.status_code, 200)

        request_create_map = self.factory.post('/map/',
                                    data={
                                        "name": get_map_template_response['name'],
                                        "map": get_map_template_response['map'],
                                    },
                                    format='json', **self.bearer_token)
        response_create_map = MapCreateAPIView.as_view()(request_create_map)
        create_map_response = response_create_map.data
        self.assertEqual(response_create_map.status_code, 201)

        request_create_game = self.factory.post('/game/',
                                                data={
                                                    "name": "test_game",
                                                    "lobby": create_lobby_response['id'],
                                                    "map": create_map_response['id']
                                                },
                                                format='json', **self.bearer_token)
        response_create_game = GameCreateAPIView.as_view()(request_create_game)
        create_game_response = response_create_game.data
        self.assertEqual(response_create_game.status_code, 201)

        request_get_current_game = self.factory.get('/game/', **self.bearer_token)
        response_get_current_game = GameAPIView.as_view()(request_get_current_game, pk=create_game_response['id'])
        self.assertEqual(response_get_current_game.status_code, 200)

        request_get_current_game_map = self.factory.get('/map/1/', **self.bearer_token)
        response_get_current_game_map = MapAPIView.as_view()(
            request_get_current_game_map,
            id=create_game_response['map']
        )
        self.assertEqual(response_get_current_game_map.status_code, 200)
