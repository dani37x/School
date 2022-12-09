from django.contrib import admin

from .models import Teacher, Student_Class, Student, Mark
from django.http import FileResponse

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


@admin.action(description='Maternity Leave')
def maternity_leave(modeladmin, request, queryset):
    queryset.update(status='maternity leave')

@admin.action(description='Teacher is availabile')
def availabile(modeladmin, request, queryset):
    queryset.update(status='availabile')

@admin.action(description='Sick leave')
def sick_leave(modeladmin, request, queryset):
    queryset.update(status='sick leave')


@admin.action(description='Generate raport as PDF')
def pdf_generator(modeladmin, request, queryset):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text = c.beginText()
    text.setTextOrigin(inch, inch)
    text.setFont("Helvetica", 14)

    data = queryset
    lines = []
    for row in data:
        print(row)
        lines.append(row.first_name)
        lines.append(row.surname)
        lines.append(str(row.school_class))
        lines.append("----------------------")

    for  line in lines:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Students.pdf')


class TeacherAdmin(admin.ModelAdmin):
    list_display = [Teacher.teachers, Teacher.status_color]
    ordering = ['surname']
    actions = [maternity_leave, availabile, sick_leave, pdf_generator]


class Student_ClassAdmin(admin.ModelAdmin):
    pass
    
class MarkAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['school_class']
    search_fields = ('first_name__startswith', 'surname__startswith')
    actions = [pdf_generator]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student_Class)
admin.site.register(Student, StudentAdmin)
admin.site.register(Mark)