from django.contrib import admin

from .models import Teacher, Student_Class, Student, Mark

admin.site.register(Teacher)
admin.site.register(Student_Class)
admin.site.register(Student)
admin.site.register(Mark)