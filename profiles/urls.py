from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_redirect_view, name='profile_redirect'),
    path('job-seeker/edit/', views.JobSeekerProfileUpdateView.as_view(), name='update_job_seeker_profile'),
    path('recruiter/edit/', views.RecruiterProfileUpdateView.as_view(), name='update_recruiter_profile'),
]
