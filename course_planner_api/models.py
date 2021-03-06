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
        """Create a super user"""
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
    study_terms = JSONField(blank=True, null=True)
    current_academic_term = models.CharField(
        max_length=3, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        """return string of user"""
        return self.email


class SemesterGroup(models.Model):
    """Database model for semester groups"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )

    semester = models.CharField(max_length=12)

    def getSemesterCode(self):
        """Return int course code following waterloo open data api term structure https://github.com/uWaterloo/api-documentation/blob/master/v2/terms/list.md"""
        semester = self.semester.strip().upper()
        semester_term = "1"
        if 'WINTER' in semester:
            semester_term = "5"
        elif 'SPRING' in semester:
            semester_term = "9"
        semester_year_list = ['1']
        parsed_year_list = [s for s in semester if s.isdigit()]
        print(semester_term)
        semester_year_list = semester_year_list + parsed_year_list[2:]
        semester_year = "".join(semester_year_list)
        return int(semester_year+semester_term)

    def __str__(self):
        """Return string of semester"""
        return self.semester


class CourseItem(models.Model):
    """Database model for course items"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )

    semester_placement = models.ForeignKey(
        SemesterGroup, on_delete=models.CASCADE, blank=True, null=True
    )
    course_subject = models.CharField(max_length=10)
    course_number = models.IntegerField()
    reqs = JSONField(blank=True, null=True)
    semester_offered = JSONField(blank=True, null=True)

    def __str__(self):
        """Return string of course subject and number"""
        return f"{self.course_subject}-{self.course_number}"
