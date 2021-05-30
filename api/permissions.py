from rest_framework.permissions import BasePermission


class IsLogged(BasePermission):

    def is_authernticated(self, request, view, obj):
        return (request.user.is_authenticated)


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)
