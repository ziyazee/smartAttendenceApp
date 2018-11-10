
from django import forms
from .models import Attendence

class addStudent(forms.ModelForm):
    class Meta:
        model=Attendence
        fields=('usn','name','branch','year')
