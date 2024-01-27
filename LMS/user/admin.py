from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import MyUser, Student, Teacher

# Admin class for MyUser model
class MyUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser']

admin.site.register(MyUser, MyUserAdmin)

# Admin class for Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'roll_number']

admin.site.register(Student, StudentAdmin)

# Admin class for Teacher model
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'employee_id']

admin.site.register(Teacher, TeacherAdmin)

