from django.apps import AppConfig


class PrescreenConfig(AppConfig):
    name = 'prescreen'
    verbose_name = 'The main prescreen system'
    def ready(self):
        import prescreen.signals # Triggers signals active
        print('[Prescreen System Loaded]')