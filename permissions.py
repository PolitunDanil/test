from rest_framework import permissions
import os
from django.shortcuts import HttpResponse


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class OnlyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if (os.getenv("secretKey") == request.headers["secretKey"]):
            return True
        else:
            return HttpResponse({"u have not a Key"})
