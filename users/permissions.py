from rest_framework.permissions import BasePermission

class ListOnly(BasePermission):
    def has_permission(self, request, view):
        return view.action == "list"