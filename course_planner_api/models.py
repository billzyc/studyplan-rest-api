from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings
from jsonfield import JSONField


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create a super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    required_courses = JSONField(blank=True, null=True)
    current_academic_term = models.CharField(
        max_length=3, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        """return string of user"""
        return self.email


class CourseItem(models.Model):
    """Database model for course items"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    course_subject = models.CharField(max_length=10)
    course_number = models.IntegerField()
    year_placement = models.IntegerField(blank=True, null=True)
    semester_placement = models.CharField(max_length=2, blank=True, null=True)
    reqs = JSONField(blank=True, null=True)
    semester_offered = JSONField(blank=True, null=True)

    def __str__(self):
        """Return model as course number"""
        return f"{self.course_subject}-{self.course_number}"
