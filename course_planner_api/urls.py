from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course_planner_api import views

router = DefaultRouter()
router.register("profile", views.UserProfileViewSet)
router.register("course-items", views.UserCourseItemViewSet)

urlpatterns = [
    path("login/", views.UserLoginViewSet.as_view()),
    path("", include(router.urls)),
]
