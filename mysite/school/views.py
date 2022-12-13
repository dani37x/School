from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages

from django_ratelimit.decorators import ratelimit

from .models import Student, Student_Class, Ip_address
from .forms import  SearchForm, LoginForm

from .reports import students_summary
from .reports import students_in_class

from .functions import get_client_ip


class StudentListView(ListView):
    model = Student
    paginate_by = 5
    ordering = ['surname']

    def get_context_data(self,*, object_list=None, **kwargs):
        context = object_list if object_list is not None else self.object_list
        print(context)
        form = SearchForm(self.request.GET)

        if form.is_valid():
            searching_field = form.cleaned_data.get('text','')
            sort_by = form.cleaned_data.get('sort_by','')
            sort_type = form.cleaned_data.get('sort_type','')
            if sort_type == True:
                sort = '-'
            else:
                sort = ''
            try:
                context = (
                    context.filter(first_name__icontains=searching_field)
                    | context.filter(surname__icontains=searching_field)
                    | context.filter(school_class__name=searching_field)
                ).order_by(f'{sort}{sort_by}')
            except:
                context = (
                    context.filter(first_name__icontains=searching_field)
                    | context.filter(surname__icontains=searching_field)
                    | context.filter(school_class__name=searching_field)
                )               

        return super().get_context_data(
            **kwargs,
            form=form,
            object_list=context,
            students_summary = students_summary(context=context),
        )
    
class Student_ClassListView(ListView):
    model = Student_Class
    paginate_by = 5
    ordering = ['name']

    def get_context_data(self,*,object_list=None, **kwargs):
        context = object_list if object_list is not None else self.object_list

        return super().get_context_data(
            **kwargs,
            object_list=context,
            students_in_class=students_in_class(context=context)    
        ) 
 
@ratelimit(key='ip', rate='5/m', block=False)
def accounts_login(request):
    ipv4 = get_client_ip(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user != None and user != '':
                login(request, user)
                already_logged = Ip_address.objects.all()
                counter = 0
                for log in already_logged:
                    if log.username == username:
                        counter += 1
                if counter == 3:    
                    return redirect('school:accounts-logout')
                else:
                    Ip_address(username=username, ip=ipv4).save()
                    return redirect('school:page')
            else:
                # messages.add_message(request, messages.ERROR, '[ERROR]  WRONG USERNAME OR PASSWORD')
                return redirect('school:accounts-login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def accounts_logout(request):
    print(request.user.username)
    user = Ip_address.objects.filter(username=request.user.username)
    user.delete()
    logout(request)
    return redirect('school:accounts-login')

@ratelimit(key='post:username', rate='20/m')
@ratelimit(key='ip', rate='20/m', block=False)
@login_required
def page(request):
    return HttpResponse('x')
