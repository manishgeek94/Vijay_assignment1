from django import forms
from .models import Student, Backlogs


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class BacklogsForm(forms.ModelForm):
    class Meta:
        model = Backlogs
        fields = "__all__"
