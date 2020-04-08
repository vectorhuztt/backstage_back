from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from Api.models import UserToken


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed()
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        return 'Basic realm="api"'