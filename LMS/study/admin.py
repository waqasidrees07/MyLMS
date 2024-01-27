from django.contrib import admin
from study.models import Course, Subject, Enrollment

# Admin class for Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'description']

admin.site.register(Course, CourseAdmin)

# Admin class for Subject model
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'description', 'course']

admin.site.register(Subject, SubjectAdmin)

# Admin class for Enrollment model
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'enrollment_date']

admin.site.register(Enrollment, EnrollmentAdmin)

