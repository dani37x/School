from django.contrib import admin

from .models import Teacher, Studnet_Class, Student, Mark

admin.site.register(Teacher)
admin.site.register(Studnet_Class)
admin.site.register(Student)
admin.site.register(Mark)