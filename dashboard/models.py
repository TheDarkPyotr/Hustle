from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    subject = models.CharField(max_length=100, unique=False)
    symbol = models.CharField(max_length=30, unique=True)
    cfu_number = models.PositiveIntegerField(default=6)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=300)
    next_date = models.DateTimeField(auto_now_add=False)
    teacher = models.CharField(max_length=100, unique=False, default="Prof. unkwown")
    grade = models.PositiveIntegerField(default=18)

    def __str__(self):
        return self.symbol

    def get_total_exam(self):
        return Exam.objects.filter().count()

class Schedule(models.Model):
    room = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=False)
    subject = models.ForeignKey(Exam, related_name='exam', on_delete=True)
    note = models.TextField(max_length=4000)

    def __str__(self):
        return self.room


