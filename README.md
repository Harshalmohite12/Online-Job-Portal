# NexusJobs – Online Job Portal

NexusJobs is a full-stack job board web application built with Python and Django. It connects **recruiters** and **job seekers** on a single secure platform. Recruiters can post jobs, manage listings, and review applications, while job seekers can edit their profile, search and filter jobs, and track their application statuses.

---

## 🚀 Getting Started & Running the Project

### 1. Open Terminal and Navigate to Project Root
Open PowerShell, Command Prompt, or Git Bash, and navigate to the project directory:
```powershell
cd "h:/Projects/Online Job Portal"
```

### 2. Activate the Virtual Environment
Activate the pre-configured Python virtual environment (`venv`) to load all required dependencies (Django, Pillow, mysqlclient, etc.):

* **PowerShell:**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **Command Prompt (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
* **Git Bash:**
  ```bash
  source venv/Scripts/activate
  ```

*(Once activated, you will see `(venv)` prepended to your command prompt).*

### 3. Run the Development Server
Since all database migrations are already applied to the SQLite database, you can start the server immediately:
```bash
python manage.py runserver
```
Once started, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

### 4. Create an Admin User (Optional)
To log into the Django Admin dashboard (`http://127.0.0.1:8000/admin/`) and manage database entries directly:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

---

## 👥 User Roles & Detailed Usage Guide

When a user signs up on NexusJobs, they must select one of two roles: **Job Seeker** or **Recruiter**. The interface automatically adapts to their role.

---

### 1. 💼 Recruiter User Flow

Recruiters are responsible for posting jobs and managing applicants.

#### Step 1.1: Registration & Profile Setup
* Register a new account at `/accounts/register/` and choose the **Recruiter** role.
* You will be redirected to the **Recruiter Dashboard** (`/applications/dashboard/recruiter/`).
* Go to your **Profile** (`/profiles/recruiter/edit/`) and complete your company information:
  * Company Name
  * Company Logo (Image upload)
  * Corporate Website URL
  * Industry & Location
  * Company Description
  * Public Contact Email

#### Step 1.2: Posting a Job Listing
* From the dashboard, click **Post a Job** (or navigate to `/jobs/create/`).
* Fill out the job details:
  * **Job Title:** (e.g., *Senior Django Developer*)
  * **Job Type:** Select *Full-time*, *Part-time*, *Internship*, or *Remote*.
  * **Location:** (e.g., *Remote* or *San Francisco, CA*)
  * **Salary Range:** (e.g., *$90,000 - $120,000*)
  * **Application Deadline:** (Date format)
  * **Description & Requirements:** Full description of responsibilities and skill requirements.
* Click **Submit** to publish the job post.

#### Step 1.3: Managing Job Listings & Applicants
* The Recruiter Dashboard shows all jobs you have posted.
* For each job, you can **Edit** details or **Delete** the post.
* Click on **View Applicants** next to any job (or go to `/applications/job/<id>/applicants/`) to see candidates who applied.
* **Applicant Review Dashboard:**
  * View candidates' details (Name, Skills, Education, Work Experience).
  * Download the applicant's uploaded PDF Resume.
  * Update the Application Status (dropdown menu: `Pending` → `Reviewed` → `Shortlisted` → `Rejected`).

---

### 2. 🔍 Job Seeker User Flow

Job Seekers can search, apply for jobs, and monitor their applications.

#### Step 2.1: Registration & Profile Setup
* Register a new account at `/accounts/register/` and choose the **Job Seeker** role.
* You will be redirected to the **Job Seeker Dashboard** (`/applications/dashboard/job-seeker/`).
* Navigate to your **Profile** (`/profiles/job-seeker/edit/`) to build your CV:
  * Phone Number & Profile Photo
  * Resume (Upload a PDF file)
  * Skills (Input as comma-separated values, e.g., `Python, Django, SQL, Git`)
  * Education details
  * Work Experience description

#### Step 2.2: Browsing & Searching for Jobs
* Click **Browse Jobs** in the navbar (or visit `/jobs/`).
* **Search / Filter Bar:**
  * Search by **Keyword** (filters job titles).
  * Filter by **Location** (filters job locations).
* Click on any job card to view the full details page, including description, requirements, company info, and application deadline.

#### Step 2.3: Applying for a Job
* On the Job Details page, click **Apply Now**.
* You have two options:
  * Apply using your **Default Profile Resume** (already uploaded to your profile).
  * Upload a **New Resume** specifically for this application.
* Click **Submit Application**.
* *Note: The portal prevents duplicate applications to the same job post. If you try to apply again, a warning message will appear.*

#### Step 2.4: Tracking Application Statuses
* Go to your **Job Seeker Dashboard** to see all jobs you have applied for.
* Check the **Status** column to track recruiter feedback:
  * 🟡 **Pending:** Application received, awaiting recruiter review.
  * 🔵 **Reviewed:** Recruiter has opened and reviewed your application.
  * 🟢 **Shortlisted:** You have been selected for next steps/interview.
  * 🔴 **Rejected:** Application did not meet current requirements.

---

## 🏗️ Codebase & Database Architecture

The project is structured with modular Django apps:

1. **`accounts`**: Custom user registrations, login, logout, and role selections.
   * Model: [User](file:///h:/Projects/Online%20Job%20Portal/accounts/models.py) (Extends `AbstractUser`, adds `role`).
   * Views: [views.py](file:///h:/Projects/Online%20Job%20Portal/accounts/views.py).
2. **`profiles`**: Individual profile storage for job seekers and recruiters.
   * Models: [JobSeekerProfile](file:///h:/Projects/Online%20Job%20Portal/profiles/models.py#L4-L14) and [RecruiterProfile](file:///h:/Projects/Online%20Job%20Portal/profiles/models.py#L16-L27).
   * Views: [views.py](file:///h:/Projects/Online%20Job%20Portal/profiles/views.py).
3. **`jobs`**: Job postings, job search engine, and editing listings.
   * Model: [Job](file:///h:/Projects/Online%20Job%20Portal/jobs/models.py) (Links to `RecruiterProfile`).
   * Views: [views.py](file:///h:/Projects/Online%20Job%20Portal/jobs/views.py).
4. **`applications`**: Application submissions, dashboard management, and status updates.
   * Model: [Application](file:///h:/Projects/Online%20Job%20Portal/applications/models.py) (Links `Job` and `JobSeekerProfile`; uses a unique constraint to prevent duplicates).
   * Views: [views.py](file:///h:/Projects/Online%20Job%20Portal/applications/views.py).
5. **`job_portal`**: Central configuration app.
   * Core configurations: [settings.py](file:///h:/Projects/Online%20Job%20Portal/job_portal/settings.py).
   * Main URL routing: [urls.py](file:///h:/Projects/Online%20Job%20Portal/job_portal/urls.py).
