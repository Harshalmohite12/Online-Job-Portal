from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:pk>/', views.ApplyJobView.as_view(), name='apply_job'),
    path('dashboard/job-seeker/', views.JobSeekerDashboardView.as_view(), name='job_seeker_dashboard'),
    path('dashboard/recruiter/', views.RecruiterDashboardView.as_view(), name='recruiter_dashboard'),
    path('job/<int:pk>/applicants/', views.JobApplicantsView.as_view(), name='job_applicants'),
    path('update-status/<int:pk>/', views.ApplicationUpdateStatusView.as_view(), name='update_application_status'),
]
