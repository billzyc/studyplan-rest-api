from rest_framework import serializers

from course_planner_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile"""

    class Meta:
        model = models.UserProfile
        fields = (
            "id",
            "email",
            "name",
            "password",
            "required_courses",
            "current_academic_term",
            "study_terms"
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)


class CourseItemSerializer(serializers.ModelSerializer):
    """Serializers course information"""

    class Meta:
        model = models.CourseItem
        fields = (
            "id",
            "user_profile",
            "course_subject",
            "course_number",
            "term_placement",
            "reqs",
            "semester_offered",
        )
        extra_kwargs = {"user_profile": {"read_only": True}}
