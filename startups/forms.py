from django import forms
from django.forms import ModelForm
from .models import Startups, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("title","company","contact","location","description","company_logo","date")
        widgets ={
            'title':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;left:300px', 'class': 'form-control'}),
            'company':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'contact':forms.NumberInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'location':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            # 'company_logo':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'date':forms.DateInput(attrs={'placeholder':'Format:YYYY-MM-DD', 'style': 'width: 60%;', 'class': 'form-control'}),
        }
class StartupsForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 40%;', 'class': 'form-control'}))
    # contact = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 40%;', 'class': 'form-control'}))
    class Meta:
        model = Startups
        fields = ("name","specialty","contact","location","description","image","website")
        widgets ={
            'name':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'contact':forms.NumberInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'specialty':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'location':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            # 'image':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
            'website':forms.TextInput(attrs={'placeholder':'Name', 'style': 'width: 60%;', 'class': 'form-control'}),
        }        