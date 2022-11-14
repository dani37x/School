from django.db import models

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

class Teacher(models.Model):
    first_name = models.CharField(blank=False, max_length=256)
    surname = models.CharField(blank=False, max_length=256)

    def __str__(self):
        return f'{self.first_name} {self.surname}'

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Studnet_Class(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=256)
    special_class = models.BooleanField(default=False)
    educator = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student Class'
        verbose_name_plural = 'Student Classes'

class Student(models.Model):
    first_name = models.CharField(blank=False, max_length=256)
    surname = models.CharField(blank=False, max_length=256)
    disability = models.BooleanField(default=False)
    age = models.IntegerField(default=6, blank=False)
    school_class = models.ForeignKey(Studnet_Class, on_delete=models.DO_NOTHING)
    #change

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
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    teachar = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.mark}: {self.mark_type.upper()} from {self.subject.upper()} - {self.student}'
        
    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'





