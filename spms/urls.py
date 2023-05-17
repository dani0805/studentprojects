"""
urls for spms app
"""
from django.urls import path
from spms import views

urlpatterns = [
    path('student/', views.StudentList.as_view(), name='student_list'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
    path('project/', views.ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>/createtask/', views.ProjectTaskCreateView.as_view(), name='project_task_create'),
    path('task/', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('taskfile/', views.TaskFileList.as_view(), name='taskfile_list'),
    path('taskfile/<int:pk>/', views.TaskFileDetail.as_view(), name='taskfile_detail'),
    path('taskfile/create/', views.TaskFileCreate.as_view(), name='taskfile_create'),
    path('taskfile/<int:pk>/update/', views.TaskFileUpdate.as_view(), name='taskfile_update'),
    path('taskfile/<int:pk>/delete/', views.TaskFileDelete.as_view(), name='taskfile_delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('rest/student/', views.StudentViewSet.as_view({'get': 'list'}), name='student_list'),
    # catch all for anything not matched above
    path('', views.StudentList.as_view(), name='student_list'),
]
