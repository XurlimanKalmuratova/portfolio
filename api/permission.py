from rest_framework.permissions import BasePermission

       


class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'DELETE']:
            return request.user.is_authenticated    