class BaseAuthentication:
    unauthorized_message = {"error": "Unauthorized"}

    def authenticate(self, request, handler, *args, **kwargs):
        return True
