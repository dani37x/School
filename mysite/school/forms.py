from django import forms

from .models import Student


class LoginForm(forms.Form):
    username =  forms.CharField(
        label='Username',
        max_length=25,
        )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        max_length=50,
        )


SORTING = (
('first_name', 'first name'),
('surname', 'surname'),
('school_class', 'class'),
)

class SearchForm(forms.Form):
    text = forms.CharField(
        max_length=100,
        label='What do you need?',
        )
    sort_by = forms.CharField(
        widget=forms.Select(choices=SORTING),
        label='Sort by',
        # initial='surname',
        )
    sort_type = forms.BooleanField(
        label='Descending sorting',
        # initial='-'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['sort_by'].required = False
        self.fields['sort_type'].required = False


# Form with model from database
# class StudentSearchForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields =('first_name',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['first_name'].required = False
