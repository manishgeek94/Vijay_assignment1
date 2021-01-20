from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_id = models.IntegerField(primary_key=True)
    student_school = models.TextField()

    def __str__(self):
        return self.student_name


class Backlogs(models.Model):
    active_backlogs = models.IntegerField()
    B_id = models.ForeignKey(Student, on_delete=models.CASCADE,primary_key=True)


