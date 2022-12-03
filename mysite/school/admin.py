from django.contrib import admin

from .models import Teacher, Student_Class, Student, Mark



@admin.action(description='Maternity Leave')
def maternity_leave(modeladmin, request, queryset):
    queryset.update(status='maternity leave')

@admin.action(description='Teacher is availabile')
def availabile(modeladmin, request, queryset):
    queryset.update(status='availabile')

@admin.action(description='Sick leave')
def sick_leave(modeladmin, request, queryset):
    queryset.update(status='sick leave')

class TeacherAdmin(admin.ModelAdmin):
    list_display = [Teacher.teachers, Teacher.status_color]
    ordering = ['surname']
    actions = [maternity_leave, availabile, sick_leave]

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student_Class)
admin.site.register(Student)
admin.site.register(Mark)