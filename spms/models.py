"""
Students extend the User model with a profile, which contains their university, major, and year, and a list of projects
Projects have a title, description, and a list of students
Each project has a list of tasks, which have a title, description, and a list of students and a list of files
Files have a title, description, and a file and a type (e.g. code, report, etc.)
"""

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models import PROTECT
from django.urls import reverse


class Student(AbstractUser):
    university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    year = models.IntegerField(default=1)


    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.username + ")"

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    students = models.ManyToManyField(Student, related_name="projects")

    def __str__(self):
        return self.title

    def create_tasks(self):
        for i in range(10000):
            Task.objects.create(title="Task " + str(i), description="Task " + str(i), project=self, deadline="2019-12-31 23:59:59", created_by=self.students.all()[0])


    def get_absolute_url(self):
        return reverse('project_list')


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    students = models.ManyToManyField(Student, related_name="students")
    project = models.ForeignKey(Project, on_delete=PROTECT, null=True, related_name="tasks")
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(Student, on_delete=PROTECT, null=True, related_name="created_tasks")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskFile(models.Model):
    FILE_TYPES = (
        ('code', 'Code'),
        ('report', 'Report'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    file = models.FileField()
    task = models.ForeignKey(Task, on_delete=PROTECT, null=True, related_name="files")
    type = models.CharField(max_length=100, choices=FILE_TYPES)

    def __str__(self):
        return self.title



