from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Teacher)
admin.site.register(models.Course)
admin.site.register(models.CourseCategory)
admin.site.register(models.Student)
# admin.site.site_header = "LMS Admin"
