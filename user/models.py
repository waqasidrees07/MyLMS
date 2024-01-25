from django.db import models
from django.contrib.auth.models import AbstractUser
from study.models import Course, Subject


class MyUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    