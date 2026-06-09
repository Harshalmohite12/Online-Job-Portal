from django import forms
from .models import JobSeekerProfile, RecruiterProfile

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['phone_number', 'resume', 'skills', 'education', 'work_experience', 'profile_photo']

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ['company_name', 'company_logo', 'website', 'industry', 'location', 'company_description', 'contact_email']
