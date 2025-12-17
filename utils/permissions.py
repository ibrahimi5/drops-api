from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests for anyone
        if request.method in SAFE_METHODS:
            return True

        # Write access only for the owner
        return obj.owner == request.user