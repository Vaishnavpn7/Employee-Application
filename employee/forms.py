from django import forms
from api.models import Employees


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
