from django.db import models
from django.apps import apps


# Model for Course
class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.get_full_name()} enrolled in {self.course.name}"
    

# Model for Subject
class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name
