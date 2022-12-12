from django.db import models

from django.utils.html import format_html

TEST_CHOICES = [
    ('quiz', 'quiz'),
    ('exam', 'exam'),
    ('text', 'test'),
    ('oral', 'oral')
]

SCHOOL_SUBJECTS = [
    ('english', 'english'),
    ('history', 'history'),
    ('PE', 'PE'),
    ('math', 'math'),
    ('economy', 'economy'),
    ('geography', 'geography'),
    ('psychics', 'psychics'),
]
SEX_CHOICE = [
    ('girl', 'girl'),
    ('boy', 'boy'),
]

STATUS_LIST = [
    ('maternity_leave', 'maternity leave'),
    ('sick_leave', 'sick leave'),
    ('availabile', 'availabile'),
]

class Teacher(models.Model):
    first_name = models.CharField(blank=False, max_length=256)
    surname = models.CharField(blank=False, max_length=256)
    status =  models.CharField(choices=STATUS_LIST, max_length=256)

    def __str__(self):
        return f'{self.first_name} {self.surname}'

    def teachers(self):
        return f'{self.first_name} {self.surname}'

    def status_color(self):
        color = 'blue'
        if self.status == 'availabile':
            color = 'green'
        if self.status == 'maternity_leave':
            color = 'red'
        return format_html(
            f'<span style="color:{color}"> {self.status} </span>'
        )

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Student_Class(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=256)
    special_class = models.BooleanField(default=False)
    educator = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student Class'
        verbose_name_plural = 'Student Classes'

class Student(models.Model):
    first_name = models.CharField(blank=False, max_length=256)
    surname = models.CharField(blank=False, max_length=256)
    sex = models.CharField(choices=SEX_CHOICE,  blank=False, max_length=256)
    disability = models.BooleanField(default=False)
    age = models.IntegerField(default=6, blank=False)
    school_class = models.ForeignKey(Student_Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.surname} {self.school_class}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Mark(models.Model):
    mark = models.IntegerField(default=5, blank=False)
    mark_type = models.CharField(choices=TEST_CHOICES, blank=False, max_length=256)
    weight = models.IntegerField(default=2)
    subject = models.CharField(choices=SCHOOL_SUBJECTS, max_length=256)
    pub_date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_constraint=False)
    teachar = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f'{self.mark}: {self.mark_type.upper()} from {self.subject.upper()} - {self.student}'
        
    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'


class Ip_address(models.Model):
    username = models.CharField(blank=False, max_length=256)
    ip = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return f'{self.username} - {self.ip}'

    class Meta:
        verbose_name = 'Ip_address'
        verbose_name_plural = 'Ip_addresses'



