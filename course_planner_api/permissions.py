from rest_framework import permissions


class UpdateUserProfile(permissions.BasePermission):
    """allows users to edit profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access a profile"""
        if request.user.is_staff:
            return True
        else:
            return obj.id == request.user.id


class UpdateSemesterGroup(permissions.BasePermission):
    """allows users to edit semester info"""

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access a semester"""

        if request.user.is_staff:
            return True
        else:
            return obj.user_profile.email == request.user.email


class UpdateCourseItem(permissions.BasePermission):
    """allows users to edit course list"""

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access a course list"""

        if request.user.is_staff:
            return True
        else:
            return obj.user_profile.email == request.user.email
