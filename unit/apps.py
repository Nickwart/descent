from django.apps import AppConfig


class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unit'


def get_model(param, skill_class_name):
    return None