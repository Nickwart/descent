from game.models import Map, Game
from game.views import GameCreateAPIView, GameAPIView, MapCreateAPIView, MapTemplateAPIView, MapAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from django.test import TestCase
from lobby.models import Lobby


class GameTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_user = User.objects.create_user(
            username='test_user',
            email='qqq@gmail.com',
            password='bananana'
        )
        self.lobby = Lobby.objects.create(
            name='test_lobby',
            private=False,
            password='bananana',
            creator=self.test_user)
        self.map_data = {
            'id': 1,
            'name': 'first_blood_dev',
            'map': [
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'B', 'F', 'F', 'B', 'S', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'B', 'F', 'F', 'B', 'S', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'F', 'F', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'F', 'W', 'W', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'F', 'W', 'W', 'W', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'F', 'W', 'W', 'W', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'F', 'F', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']],
            'creator': 1,
            'type': 'DV'
        }
        self.map = Map.objects.create(
            name='first_blood_dev',
            map=self.map_data['map']
            # [
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'B', 'F', 'F', 'B', 'S', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'B', 'F', 'F', 'B', 'S', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'F', 'F', 'S', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'F', 'W', 'W', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'F', 'W', 'W', 'W', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'F', 'W', 'W', 'W', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'F', 'F', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'B', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'F', 'F', 'F', 'F', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'F', 'F', 'F', 'F', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'B', 'B', 'B', 'B', 'B', 'B', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            #     ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']],
            )
        self.game = Game.objects.create(
            name='default_test_game',
            lobby=Lobby.objects.create(
                name='default_test_lobby',
                private=False,
                password='bananana',
                creator=self.test_user
                )
        )

    @property
    def bearer_token(self):
        refresh = RefreshToken.for_user(self.test_user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_map_template_get(self):
        request = self.factory.get('/map_template/', **self.bearer_token)
        response = MapTemplateAPIView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_map_creates(self):
        request = self.factory.post('/map/',
                                    data={
                                        "name": self.map_data['name'],
                                        "map": self.map_data['map'],
                                    },
                                    format='json', **self.bearer_token)
        response = MapCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_map_returns(self):
        request = self.factory.get('/map/1/', **self.bearer_token)
        response = MapAPIView.as_view()(request, id=1)
        self.assertEqual(response.status_code, 200)

    def test_game_creates(self):
        request = self.factory.post('/game/',
                                    data={
                                        "name": "test_game",
                                        "lobby": self.lobby.id,
                                        "map": self.map.id
                                    },
                                    format='json', **self.bearer_token)
        response = GameCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_get_all_games(self):
        request = self.factory.get('/game/', **self.bearer_token)
        response = GameCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get_current_game(self):
        request = self.factory.get('/game/', **self.bearer_token)
        response = GameAPIView.as_view()(request, pk=self.game.id)
        self.assertEqual(response.status_code, 200)
