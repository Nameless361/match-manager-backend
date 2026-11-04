from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyOrSuperuser(BasePermission):
    """
    Anyone can read.
    Only authenticated superusers can write.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )