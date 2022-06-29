from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('tasks/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('users/', views.userList, name='user-list'),  
    path('about/', views.about, name='about-view'),  
]
