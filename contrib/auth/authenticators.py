class BaseAuthentication:
    unauthorized_message = {"error": "Unauthorized"}

    async def authenticate(self, request, handler, *args, **kwargs):
        return True
