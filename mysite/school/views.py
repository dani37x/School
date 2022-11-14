from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Student
from .forms import StudentSearchForm

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class StudentListView(ListView):
    model = Student
    paginate_by = 5

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
                    context.filter(first_name=searching_field)
                    | context.filter(surname=searching_field)
                    | context.filter(school_class__name=searching_field)
                )

            # if object_list != None:
            #     print(searching_field)
        return super().get_context_data(**kwargs, form=form, object_list=context)
    