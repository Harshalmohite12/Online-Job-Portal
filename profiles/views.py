from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import JobSeekerProfile, RecruiterProfile
from .forms import JobSeekerProfileForm, RecruiterProfileForm
from django.shortcuts import redirect

class JobSeekerProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = JobSeekerProfile
    form_class = JobSeekerProfileForm
    template_name = 'profiles/job_seeker_profile_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        profile, created = JobSeekerProfile.objects.get_or_create(user=self.request.user)
        return profile

class RecruiterProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = RecruiterProfile
    form_class = RecruiterProfileForm
    template_name = 'profiles/recruiter_profile_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        profile, created = RecruiterProfile.objects.get_or_create(user=self.request.user)
        return profile

def profile_redirect_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    if not user.role:
        if user.is_superuser:
            user.role = 'RECRUITER'
            user.save()
            RecruiterProfile.objects.get_or_create(user=user)
        else:
            return redirect('home')

    if user.role == 'JOB_SEEKER':
        return redirect('update_job_seeker_profile')
    elif user.role == 'RECRUITER':
        return redirect('update_recruiter_profile')
    return redirect('home')
