# Online Job Portal – Project Prompt

## Project Overview

Build a full-stack **Online Job Portal** web application that connects **job seekers** and **recruiters** on a single secure platform. The application should allow recruiters to post jobs and manage applications, while job seekers can search, apply, and track their applications.

---

## Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Django (OOP-based) |
| Database   | MySQL                   |
| Frontend   | HTML, CSS, JavaScript   |

---

## Core Features to Implement

### 1. Authentication System
- User registration with **two roles**: `Job Seeker` and `Recruiter`
- Login / Logout with Django's built-in authentication
- Password hashing and session management
- Role-based access control (recruiters can't apply; job seekers can't post)

---

### 2. Profile Management
**Job Seeker Profile:**
- Full name, email, phone number
- Upload resume (PDF)
- Skills, education, work experience fields
- Profile photo upload

**Recruiter / Company Profile:**
- Company name, logo, website
- Industry, location, company description
- Contact email

---

### 3. Job Posting (Recruiter)
- Create a job listing with:
  - Job title, description, requirements
  - Job type (Full-time / Part-time / Internship / Remote)
  - Location, salary range
  - Application deadline
- Edit and delete own job postings
- View list of applicants per job

---

### 4. Job Search & Application (Job Seeker)
- Browse all active job listings
- Search/filter by keyword, location, job type, salary
- View full job details page
- Apply to a job (attach resume / use profile resume)
- Prevent duplicate applications to the same job

---

### 5. Application Tracking
**Job Seeker side:**
- Dashboard showing all jobs applied to
- Application status: `Pending` → `Reviewed` → `Shortlisted` → `Rejected`

**Recruiter side:**
- View all applicants for each job posting
- Update application status for each candidate
- Download applicant's resume

---

### 6. MySQL Database (CRUD Operations)
Design and implement the following tables:
- `users` – stores all user accounts with role
- `profiles` – job seeker and recruiter profile data
- `jobs` – job listings posted by recruiters
- `applications` – job seeker applications linked to jobs
- Use Django ORM for all database interactions
- Apply relationships: ForeignKey, OneToOne, ManyToMany where appropriate

---

### 7. Dashboard Pages
**Job Seeker Dashboard:**
- Recommended jobs
- Applied jobs with statuses
- Profile completion indicator

**Recruiter Dashboard:**
- Posted jobs list
- Total applicants count
- Quick status update for applications

---

## Django App Structure (Suggested)

```
job_portal/
├── accounts/       # Registration, login, logout, roles
├── profiles/       # Job seeker & recruiter profile models + views
├── jobs/           # Job posting, listing, search, detail views
├── applications/   # Apply, track, status update logic
├── templates/      # HTML templates (base, dashboard, forms)
├── static/         # CSS, JS, images
└── job_portal/     # settings.py, urls.py, wsgi.py
```

---

## OOP Principles to Apply

- Use **Class-Based Views (CBVs)** in Django wherever appropriate (e.g., `CreateView`, `UpdateView`, `ListView`, `DetailView`)
- Define clean **Model classes** with methods (e.g., `__str__`, `get_absolute_url`)
- Use Django **forms or ModelForms** as form classes
- Keep business logic inside model methods or service classes, not in views

---

## UI Pages Required

| Page                  | Description                              |
|-----------------------|------------------------------------------|
| Home / Landing        | Portal intro, search bar, featured jobs  |
| Register / Login      | Role selection during signup             |
| Job Seeker Dashboard  | Applied jobs, profile, recommendations   |
| Recruiter Dashboard   | Posted jobs, applicant management        |
| Job Listing Page      | Search + filter all jobs                 |
| Job Detail Page       | Full job info + Apply button             |
| Profile Page          | View & edit own profile                  |
| Application Status    | Job seeker tracks their applications     |

---

## Security Requirements

- CSRF protection on all forms (Django handles this by default)
- Login required for applying, posting, and dashboard access (`@login_required`)
- Users can only edit/delete their own data
- File upload validation for resumes (PDF only, size limit)

---

## Database Configuration (MySQL)

In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'job_portal_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Install: `pip install mysqlclient`

---

## Deliverables Checklist

- [ ] Working Django project with MySQL connected
- [ ] Two-role authentication (Job Seeker & Recruiter)
- [ ] Job Seeker: register, build profile, search jobs, apply, track status
- [ ] Recruiter: register, post jobs, view applicants, update status
- [ ] All CRUD operations functional via Django ORM
- [ ] Responsive HTML/CSS frontend with JavaScript enhancements
- [ ] Clean URL structure and navigation between pages

---

*This project demonstrates full-stack web development with Django, MySQL integration, authentication, role-based access, and OOP principles — suitable for a portfolio and interview demonstration.*
