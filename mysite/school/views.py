from django.views.generic.list import ListView

from .models import Student, Student_Class
from .forms import StudentSearchForm

from .reports import students_summary
from .reports import students_in_class

class StudentListView(ListView):
    model = Student
    paginate_by = 5
    ordering = ['surname']


    def get_context_data(self,*, object_list=None, **kwargs):
        context = object_list if object_list is not None else self.object_list
        form = StudentSearchForm(self.request.GET)
        if form.is_valid():
            searching_field = form.cleaned_data.get('first_name', '')
            try:
                int_value = int(searching_field)
                context = context.filter(age=int_value)
            except:
                context = (
                    context.filter(first_name__icontains=searching_field)
                    | context.filter(surname__icontains=searching_field)
                    | context.filter(school_class__name=searching_field)
                )
                # print(object_list)
                # print(context)
        return super().get_context_data(
            **kwargs,
            form=form,
            object_list=context,
            students_summary = students_summary(context=context)
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