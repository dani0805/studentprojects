# REST serializers

from rest_framework import serializers
from spms.models import Student, Task, TaskFile


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



