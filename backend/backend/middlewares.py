from channels.middleware import BaseMiddleware
from asgiref.sync import sync_to_async


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def get_user_from_token(self, token):
        from django.contrib.auth.models import User

        try:
            user_id = token.payload.get("user_id")
            if user_id:
                return await sync_to_async(User.objects.get)(pk=user_id)
        except User.DoesNotExist:
            pass
        return None

    async def __call__(self, scope, receive, send):
        from django.contrib.auth.models import AnonymousUser
        from rest_framework_simplejwt.tokens import AccessToken

        try:
            token_str = dict(scope["headers"])[b"sec-websocket-protocol"].slice(", ")[1]
            token = await sync_to_async(AccessToken)(token_str.decode())
            user = await self.get_user_from_token(token)
        except:
            token = None
        scope["user"] = user if user else AnonymousUser()
        return await super().__call__(scope, receive, send)
