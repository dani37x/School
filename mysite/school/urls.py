from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import path, reverse_lazy

from . import views
from .models import Student

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
        success_url=reverse_lazy('school:student-update'),
        template_name='generic_update.html'
        ),
        name='school-update'),

]