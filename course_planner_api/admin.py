from django.contrib import admin
from course_planner_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.CourseItem)
