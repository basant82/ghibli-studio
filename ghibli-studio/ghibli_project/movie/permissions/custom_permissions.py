from rest_framework import permissions
from django.conf import settings


class GhibliApiPermissions(permissions.BasePermission):
    """ "
    Custom permission class for Ghibli api
    """

    def has_permission(self, request, view):
        """
        return true if Authorization provided in headers of request is correct
        """
        return request.headers.get("Authorization") == settings.GHIBLI_AUTH_KEY
