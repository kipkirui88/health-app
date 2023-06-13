from django import forms
from django.forms import ModelForm
from .models import Startups, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("title","company","contact","location","description","company_logo","date")
        widgets ={
            'title':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;left:300px', 'class': 'form-control'}),
               'date':forms.DateInput(attrs={'placeholder':'Format:YYYY-MM-DD', 'style': 'width: 60%;', 'class': 'form-control'}),
        }
