from rest_framework.permissions import BasePermission

class ListAndRetrieveOnly(BasePermission):
    def has_permission(self, request, view):
        return view.action in ["list", "retrieve"]