import uuid

from descent_web_core.web_exceptions import UserNotLoggedInException, AlreadyInCurrentLobbyException
from descent_web_core.authentication import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import LobbyUser, Lobby
from django.http import HttpResponse
from django.views import View
import json


class LobbyView(View):

    def get(self, request, **kwargs):
        if authenticate(request):
            user = authenticate(request)[0]
            if user.is_staff or user.is_superuser:
                all_lobby = Lobby.objects.all().filter(**kwargs)
                return HttpResponse(all_lobby, status=200)
            else:
                all_lobby = Lobby.objects.all().filter(private=False, **kwargs)
                return HttpResponse(all_lobby, status=200)
        else:
            raise UserNotLoggedInException

    def post(self, request):
        if authenticate(request):
            user = authenticate(request)[0]
            data = json.loads(request.body)
            lobby = Lobby.objects.create(
                name=data['name'],
                private=data['private'],
                password=data['password'],
                creator=User.objects.get(id=user.id)
            )
            LobbyUser.objects.create(lobby=Lobby.objects.get(id=lobby.id), user=User.objects.get(id=user.id))
            response = json.dumps({'id': str(Lobby.objects.get(id=lobby.id).id)})
            # here in response have to be serializer

            return JsonResponse(response, status=201, safe=False)
            # return HttpResponse(responce, content_type="application/json")
        else:
            raise UserNotLoggedInException


class LobbyListCreateView(View):

    def get(self, request, lobby):
        if authenticate(request):
            lobby_ = Lobby.objects.get(id=lobby)
            lobby_users = LobbyUser.objects.filter(lobby=lobby)
            return HttpResponse({"creator - ": lobby_.creator, "users - ": lobby_users})
        else:
            raise UserNotLoggedInException

    def put(self, request, lobby):
        pass

    def patch(self, request, lobby):
        pass

    def delete(self, request, lobby):
        if authenticate(request):
            user = authenticate(request)[0]
            if user.is_staff or Lobby.objects.get(id=lobby, creator=user):
                Lobby.objects.get(id=lobby).delete()
                return HttpResponse(status=200)
        else:
            raise UserNotLoggedInException


class LobbyUserViews(View):

    def get(self, request, **kwargs):
        if not authenticate(request):
            raise UserNotLoggedInException
        else:
            response = LobbyUser.objects.all().filter(**kwargs)
            return HttpResponse(response)

    def post(self, request):
        if authenticate(request):
            data = json.loads(request.body)
            user = authenticate(request)
            lobby_id = uuid.UUID(data['lobby_id'])

            if LobbyUser.objects.filter(lobby=lobby_id, user_id=User.objects.get(username=user[0])):
                raise AlreadyInCurrentLobbyException

            if LobbyUser.objects.filter(lobby=lobby_id).count() <= 4:
                LobbyUser.objects.create(lobby=Lobby.objects.get(
                    id=lobby_id),
                    user=User.objects.get(username=user[0])
                )
                return HttpResponse(LobbyUser.objects.filter(lobby=lobby_id))
            else:
                return HttpResponse(status=403, content={"message": "pisun vpope"})

        else:
            raise UserNotLoggedInException


class LobbyUserListCreateView(View):

    def get(self, request, lobby):
        if not authenticate(request):
            raise UserNotLoggedInException
        else:
            return HttpResponse(LobbyUser.objects.all().filter(lobby=lobby))

    def put(self, request, lobby):
        pass

    def patch(self, request, lobby):
        pass

    def delete(self, request, lobby):
        if authenticate(request):
            user = authenticate(request)[0]
            LobbyUser.objects.filter(lobby_id=lobby, user_id=user.id).delete()
            return HttpResponse(status=200)
        else:
            raise UserNotLoggedInException

