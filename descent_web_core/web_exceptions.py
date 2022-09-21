from django.core.exceptions import PermissionDenied


class UserNotLoggedInException(PermissionDenied):
    pass


class AlreadyInCurrentLobbyException(PermissionDenied):
    pass


class ToManyUsersInLobbyException(PermissionDenied):
    pass
