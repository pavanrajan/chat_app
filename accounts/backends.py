from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    """
    Authenticate using email instead of username
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username  # Django sends email as "username"

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
