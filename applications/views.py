from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Application
from jobs.models import Job

class JobSeekerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'JOB_SEEKER'

class RecruiterRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'RECRUITER'

class ApplyJobView(LoginRequiredMixin, JobSeekerRequiredMixin, View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        profile = request.user.job_seeker_profile
        
        if Application.objects.filter(job=job, applicant=profile).exists():
            messages.warning(request, "You have already applied for this job.")
        else:
            resume = request.FILES.get('resume')
            if not resume:
                resume = profile.resume
            Application.objects.create(job=job, applicant=profile, resume=resume)
            messages.success(request, "Successfully applied for the job.")
        return redirect('job_detail', pk=pk)

class JobSeekerDashboardView(LoginRequiredMixin, JobSeekerRequiredMixin, ListView):
    model = Application
    template_name = 'dashboards/job_seeker_dashboard.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user.job_seeker_profile).order_by('-applied_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_jobs'] = Job.objects.all()[:5] 
        return context

class RecruiterDashboardView(LoginRequiredMixin, RecruiterRequiredMixin, ListView):
    model = Job
    template_name = 'dashboards/recruiter_dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user.recruiter_profile).order_by('-created_at')

class ApplicationUpdateStatusView(LoginRequiredMixin, RecruiterRequiredMixin, View):
    def post(self, request, pk):
        application = get_object_or_404(Application, pk=pk)
        if application.job.recruiter != request.user.recruiter_profile:
            messages.error(request, "Permission denied.")
            return redirect('recruiter_dashboard')
            
        new_status = request.POST.get('status')
        if new_status in dict(Application.STATUS_CHOICES).keys():
            application.status = new_status
            application.save()
            messages.success(request, "Status updated successfully.")
        return redirect('job_applicants', pk=application.job.pk)

class JobApplicantsView(LoginRequiredMixin, RecruiterRequiredMixin, ListView):
    model = Application
    template_name = 'applications/job_applicants.html'
    context_object_name = 'applications'

    def get_queryset(self):
        self.job = get_object_or_404(Job, pk=self.kwargs['pk'], recruiter=self.request.user.recruiter_profile)
        return Application.objects.filter(job=self.job).order_by('-applied_at')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        return context
