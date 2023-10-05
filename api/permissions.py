from rest_framework import permissions

class PeepsUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user in obj.users