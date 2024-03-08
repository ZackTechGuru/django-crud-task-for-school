from django import forms
from MyApp.models import School
class School(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
