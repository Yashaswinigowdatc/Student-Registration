from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import StudentRegistration



class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'usn', 'semester', 'backlogs', 'cgpa', 'fees_paid_receipt']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))