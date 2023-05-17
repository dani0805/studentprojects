"""
CRUD form views for all models in studentprojects app
"""
from functools import reduce
from time import timezone

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Max
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework  import viewsets

from spms.serializers import StudentSerializer
from spms.forms import StudentForm, StudentCreateForm
from spms.models import *


class StudentList(ListView):
    model = Student


class StudentDetail(DetailView):
    model = Student


class StudentCreate(FormView):
    form_class = StudentCreateForm
    model = Student
    template_name = 'spms/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentUpdate(UpdateView, UserPassesTestMixin):
    form_class = StudentForm
    model = Student

    def test_func(self):
        return self.request.user.is_superuser or self.request.user == self.get_object()


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


class ProjectList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # fetch all projects and prefetch related tasks
        context = {'project_list': Project.objects.prefetch_related('tasks__files').all()}
        for project in context['project_list']:
            # count task.files.type == 'code'
            project.code_files = 0
            for task in project.tasks.all():
                for file in task.files.all():
                    if file.type == 'code':
                        project.code_files += 1
            # count task.files.type == 'code' with filter
            # project.code_files = project.tasks.filter(files__type='code').count()

            # count task.files.type == 'code' with list comprehension
            # project.code_files = sum([task.files.filter(type='code').count() for task in project.tasks.all()])
            # count task.files.type == 'code' with double list comprehension
            # project.code_files = sum([len([file for file in task.files.all() if file.type == 'code']) for task in project.tasks.all()])


        return context


class ProjectDetail(DetailView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'


class ProjectUpdate(UpdateView, LoginRequiredMixin):
    model = Project
    fields = '__all__'


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


class ProjectTaskCreateView(TemplateView):
    template_name = 'spms/project_list.html'

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        project.create_tasks()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        for project in context['project_list']:
            project.task_max = project.tasks.aggregate(Max('deadline'))['deadline__max']
        return context


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

class TaskFileList(ListView):
    model = TaskFile


class TaskFileDetail(DetailView):
    model = TaskFile


class TaskFileCreate(CreateView):
    model = TaskFile
    fields = '__all__'


class TaskFileUpdate(UpdateView):
    model = TaskFile
    fields = '__all__'


class TaskFileDelete(DeleteView):
    model = TaskFile
    success_url = reverse_lazy('taskfile_list')


class LoginView(FormView):
    template_name = 'spms/login.html'
    success_url = reverse_lazy('student_list')
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('student_list')

# REST API views


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






