from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from course_planner_api import serializers, models, permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUserProfile,)

    def get_queryset(self):
        """Retrieves profile information for logged in user"""
        queryset = self.queryset
        if self.request.user.is_staff:
            return queryset
        else:
            try:
                query_set = queryset.filter(email=self.request.user.email)
                return query_set
            except AttributeError:
                return None


class UserLoginViewSet(ObtainAuthToken):
    """Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserSemesterGroupViewSet(viewsets.ModelViewSet):
    """Handles operations on semester information"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.SemesterGroupSerializer
    queryset = models.SemesterGroup.objects.all()
    permission_classes = (permissions.UpdateSemesterGroup, IsAuthenticated)

    def get_queryset(self):
        """Retrieves saved course info for logged in user"""
        queryset = self.queryset
        if self.request.user.is_staff:
            return queryset
        query_set = queryset.filter(user_profile=self.request.user)
        return query_set

    def perform_create(self, serializer):
        """Set semester information for the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserCourseItemViewSet(viewsets.ModelViewSet):
    """Handles operations on course list"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CourseItemSerializer
    queryset = models.CourseItem.objects.all()
    permission_classes = (permissions.UpdateCourseItem, IsAuthenticated)

    def get_queryset(self):
        """Retrieves saved course information for logged in user"""
        queryset = self.queryset
        semester_query = self.request.query_params.get('semester_query')
        if self.request.user.is_staff:
            return queryset
        else:
            if(semester_query):
                if 'unassigned' in semester_query:
                    query_set = queryset.filter(
                        user_profile=self.request.user, semester_placement=None)
                else:
                    query_set = queryset.filter(
                        user_profile=self.request.user, semester_placement=semester_query)
            else:
                query_set = queryset.filter(user_profile=self.request.user)
        return query_set

    def perform_create(self, serializer):
        """Set course information for the logged in user"""
        serializer.save(user_profile=self.request.user)
