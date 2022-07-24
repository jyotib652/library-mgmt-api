from rest_framework.permissions import BasePermission
from rest_framework import permissions

# class IsAdmin(BasePermission):
class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):

   edit_methods = ("PUT", "PATCH")
   restricted_edit_methods = ("DELETE")
   single_edit_methods = ("GET", "PATCH")

   def has_permission(self, request, view):
      # if request.user.is_authenticated and request.user.is_staff:
      if request.user.is_staff:
         return True

   def has_object_permission(self, request, view, obj):
      if request.user.is_superuser:
         return True

      if request.user.is_staff and request.method not in self.edit_methods:
         return True

      if request.method in permissions.SAFE_METHODS:
         return True

      # if obj.author == request.user:
      # if obj.created_by == request.user.email:
      #    return True

      if request.user.is_staff and request.method in self.restricted_edit_methods:
         return True
      
      return False


class MemberOnly(permissions.BasePermission):
   edit_methods = ("GET", "PUT", "PATCH")

   def has_permission(self, request, view):
      if request.user.is_member:
         return True

   def has_object_permission(self, request, view, obj):
      if request.user.is_member and request.method in self.edit_methods:
         return True

      return False
      