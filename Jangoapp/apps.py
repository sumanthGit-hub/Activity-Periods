from django.apps import AppConfig


class JangoappConfig(AppConfig):
    name = 'Jangoapp'

    def ready(self):
        """ Login and Logout signals Capturing """
        from .signals import log_user_logged_in_success,log_user_logged_out,log_user_logged_in_failed