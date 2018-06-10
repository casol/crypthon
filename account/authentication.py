from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """Authenticate using an email account."""

    def authenticate(self, username=None, password=None):
        """Takes user credentials as parameters. Has to return True if
         the user has been successfully authenticated, or False otherwise."""
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Takes a user ID parameter and has to return a User object."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

