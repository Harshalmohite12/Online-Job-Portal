from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from profiles.models import JobSeekerProfile, RecruiterProfile
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.views import View

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user.role == 'JOB_SEEKER':
            JobSeekerProfile.objects.create(user=user)
        elif user.role == 'RECRUITER':
            RecruiterProfile.objects.create(user=user)
        login(self.request, user)
        return redirect('dashboard')

class HomeView(TemplateView):
    template_name = 'home.html'

class DashboardRedirectView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.role:
            if user.is_superuser:
                # Default superuser to RECRUITER so they can manage jobs immediately
                user.role = 'RECRUITER'
                user.save()
                RecruiterProfile.objects.get_or_create(user=user)
            else:
                return redirect('home')

        if user.role == 'JOB_SEEKER':
            return redirect('job_seeker_dashboard')
        elif user.role == 'RECRUITER':
            return redirect('recruiter_dashboard')
        return redirect('home')

class QuickLoginView(View):
    def get(self, request, role_choice):
        User = get_user_model()
        if role_choice == 'seeker':
            username = 'demo_seeker'
            role = 'JOB_SEEKER'
            profile_model = JobSeekerProfile
        elif role_choice == 'recruiter':
            username = 'demo_recruiter'
            role = 'RECRUITER'
            profile_model = RecruiterProfile
        else:
            return redirect('login')

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@example.com',
                'role': role,
                'is_staff': False,
                'is_superuser': False,
            }
        )
        if created:
            user.set_password('demo1234')
            user.save()

        # Ensure profile exists
        profile_model.objects.get_or_create(user=user)

        # Log the user in
        login(request, user)
        return redirect('dashboard')
