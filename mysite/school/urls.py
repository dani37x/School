from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import path, reverse_lazy

from django_ratelimit.decorators import ratelimit


from . import views
from .models import Student, Student_Class

app_name = 'school'

urlpatterns = [
    path('',  (ratelimit(key='ip', method='GET', rate='10/m'))(login_required( views.StudentListView.as_view())), name='student-list'),
    path('page/', views.page, name='page'),
    path('accounts/login/', views.accounts_login, name='accounts-login'),
    path('accounts/logout/', views.accounts_logout, name='accounts-logout'),

    # path('accounts/login/', auth_views.LoginView.as_view(
    #     template_name='login.html',
    #     next_page='school:student-list'
    #     ),
    #     name='login-page'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(
    #     # template_name='logout.html',
    #     next_page='school:student-list'
    #     ),
    #     name='logout'),

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

    path('class/', (ratelimit(key='ip', method='GET', rate='10/m'))(login_required(views.Student_ClassListView.as_view())), name='class-list'),
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