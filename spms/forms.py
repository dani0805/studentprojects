"""
Modelforms for studentprojects app
"""

from django.forms import ModelForm
from spms.models import *
from django.contrib.auth.forms import UserCreationForm


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = 'first_name', 'last_name', 'email', 'university', 'major', 'year'


class StudentCreateForm(UserCreationForm):
    class Meta:
        model = Student
        fields = 'first_name', 'last_name', 'email', 'university', 'major', 'year', 'username', 'password1', 'password2'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskFileForm(ModelForm):
    class Meta:
        model = TaskFile
        fields = '__all__'