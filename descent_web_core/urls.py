"""descent_web_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from lobby.views import LobbyView, LobbyListCreateView, LobbyUserViews, LobbyUserListCreateView
from unit.views import UnitCreateView, UnitListCreateView
from game.views import GameCreateAPIView, GameAPIView, MapCreateAPIView, MapTemplateCreateAPIView, \
    MapTemplateAPIView, MapAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('lobby/', LobbyView.as_view()),
    path('lobby/<uuid:lobby>/', LobbyListCreateView.as_view()),
    path('lobby_user/', LobbyUserViews.as_view()),
    path('lobby_user/<uuid:lobby>/', LobbyUserListCreateView.as_view()),
    path('unit/', UnitCreateView.as_view()),
    path('unit/<int:id>/', UnitListCreateView.as_view()),
    path('game/', GameCreateAPIView.as_view()),
    path('game/<int:id>/', GameAPIView.as_view()),
    path('map/', MapCreateAPIView.as_view()),
    path('map/<int:id>/', MapAPIView.as_view()),
    path('map_template/<int:pk>/', MapTemplateAPIView.as_view()),
]
