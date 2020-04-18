from rest_framework.permissions import BasePermission


class AllUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True
        return False


class ManageUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type in [2, 3]:
            return True
        return False


class AdminUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return True
        return False