from rest_framework.permissions import BasePermission

from Api.models import UserToken

def has_token(request):
    token = request._request.GET.get('token')
    if not token:
        return False
    else:
        user = UserToken.objects.filter(token=token).first()
        if user:
            return user
        return False


class AllUserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = has_token(request)
        if user:
            return True
        return False


class ManageUserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = has_token(request)
        if user and request.user.user_type in [2, 3]:
            return True
        return False


class AdminUserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = has_token(request)
        if user and request.user.user_type == 3:
            return True
        return False