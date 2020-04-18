from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from Api.models import UserToken


class Authentication(BaseAuthentication):
    def authenticate(self, request):
        token = 0
        token_param = request._request.GET.get('token')
        token_auth = request._request.META.get('HTTP_AUTHORIZATION')
        if token_param:
            token = token_param
        if token_auth:
            token = token_auth
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed()
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        return 'Basic realm="api"'