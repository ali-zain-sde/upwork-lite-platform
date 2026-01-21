from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "client_profile")


class IsFreelancer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "freelancer_profile")
