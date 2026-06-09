from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'job_type', 'location', 'salary_range', 'application_deadline']
        widgets = {
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
        }
