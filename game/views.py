import json

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from descent_web_core.authentication import authenticate
from game.models import Game, MapTemplate, Map
from django.contrib.auth.models import User
from rest_framework import serializers
from lobby.models import Lobby
from django.views import View


class GameCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55)
    lobby = serializers.PrimaryKeyRelatedField(queryset=Lobby.objects.all())
    map = serializers.PrimaryKeyRelatedField(queryset=Map.objects.all())

    class Meta:
        model = Game
        fields = '__all__'


class GameCreateAPIView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = (IsAuthenticated,)


class GameAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = (IsAuthenticated,)


class MapSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    map = serializers.JSONField()

    class Meta:
        model = Map
        fields = '__all__'


class MapCreateAPIView(ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (IsAuthenticated,)


class MapAPIView(ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (IsAuthenticated,)


class MapTemplateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=55)
    map = serializers.JSONField()
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = MapTemplate
        fields = '__all__'


class MapTemplateCreateAPIView(ListCreateAPIView):
    queryset = MapTemplate.objects.all()
    serializer_class = MapTemplateSerializer
    permission_classes = (IsAuthenticated,)


class MapTemplateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MapTemplate.objects.all()
    serializer_class = MapTemplateSerializer
    permission_classes = (IsAuthenticated,)


class UnitCoordsChange(View):
    def patch(self, request):
        if authenticate(request):
            user = authenticate(request)[0]
            data = json.loads(request.body)
