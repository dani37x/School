from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import path, reverse_lazy

from . import views
from .models import Student, Student_Class

app_name = 'school'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('school/create/',
        CreateView.as_view(
        model=Student,
        fields='__all__',
        success_url=reverse_lazy('school:student-list'),
        template_name='generic_update.html'
        ),
        name='school-create'),
    path('school/<int:pk>/update/',
        UpdateView.as_view(
        model=Student,
        fields='__all__',
        success_url=reverse_lazy('school:student-list'),
        template_name='generic_update.html'
        ),
        name='school-update'),
    path('school/<int:pk>/delete/',
        DeleteView.as_view(
        model=Student,
        success_url=reverse_lazy('school:student-list'),
        template_name='generic_delete.html'
        ),
        name='school-delete'),

    path('class/', views.Student_ClassListView.as_view(), name='class-list'),
    path('class/create/',
        CreateView.as_view(
        model=Student_Class,
        fields='__all__',
        success_url=reverse_lazy('school:class-list'),
        template_name='generic_update.html'
        ),
        name='class-create'),
    path('class/<int:pk>/update/',
        UpdateView.as_view(
        model=Student_Class,
        fields='__all__',
        success_url=reverse_lazy('school:class-list'),
        template_name='generic_update.html'
        ),
        name='class-update'),
    path('school/<int:pk>/delete/',
        DeleteView.as_view(
        model=Student_Class,
        success_url=reverse_lazy('school:class-list'),
        template_name='generic_delete.html'
        ),
        name='class-delete'),
]