from django import forms
from .models import Projects

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)