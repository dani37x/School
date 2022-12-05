from django import forms

from .models import Student

class StudentSearchForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =('first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False


CHOICES= (
('ME', '1'),
('YOU', '2'),
('WE', '3'),
)

class SearchForm(forms.Form):
    text = forms.CharField(max_length=100)
    select = forms.CharField(widget=forms.Select(choices=CHOICES))