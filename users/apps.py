from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'The main user system'
    def ready(self):
        import users.signals # Triggers signals active
        print('[User System Loaded]')