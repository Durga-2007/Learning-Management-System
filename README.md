# AI-Powered Cloud Learning Management System (LMS)

A complete, beginner-friendly Cloud Learning Management System (LMS) web application built using **Python Flask, HTML5, CSS3, Bootstrap 5, and MySQL**.

This project features a modern, responsive college-style dashboard and supports three user roles: **Student, Faculty, and Admin**. It also includes an **AI Study Companion** with a local pattern-matching fallback and optional Google Gemini cloud integration.

---

## Table of Contents
1. [Key Features](#key-features)
2. [Project Architecture (MVC)](#project-architecture-mvc)
3. [Database Schema Structure](#database-schema-structure)
4. [Prerequisites & Setup](#prerequisites--setup)
5. [How to Run the Application](#how-to-run-the-application)
6. [Default Login Credentials](#default-login-credentials)
7. [AI Study Companion Details](#ai-study-companion-details)
8. [Internship Viva Cheat Sheet](#internship-viva-cheat-sheet)

---

## Key Features

### 🔐 Multi-Role Authentication
- Secure password hashing using Werkzeug PBKDF2 encryption.
- Separate session isolation for Students, Faculty, and Admins.

### 👨‍🎓 Student Dashboard
- Browse available courses and enroll/drop instantly.
- Access uploaded notes and syllabus files.
- Download PDF/DOCX materials and upload homework submissions.
- Check assignment grading status, view scored marks, and review teacher feedback.
- Read real-time notification alerts (e.g. assignments published, homework graded).

### 👩‍🏫 Faculty Dashboard
- View assigned courses.
- Upload study notes (PDF, DOCX, ZIP, etc.) for a specific course.
- Publish assignments with descriptive requirements and due dates.
- Access submissions desk to view student uploads and award grades/write feedback.

### 🛠️ Admin Dashboard
- Track global analytics (total students, faculty staff, active courses, submissions).
- Create, read, update, and delete (CRUD) student and faculty directories.
- Register new courses and assign faculty instructors.

### 🤖 AI Study Assistant
- Sleek conversational chatbot themed around the selected course.
- Generates mock multiple-choice quizzes, course summaries, study tips, or defines computer science terms.
- Works offline (local matching) and automatically upgrades to a real LLM if a Google Gemini API key is supplied.

---

## Project Architecture (MVC)

The project is structured following the **Model-View-Controller (MVC)** design pattern, which makes it extremely clean and easy to explain in a viva:

```
LMS/
│
├── app.py                      # Main Controller: Flask Router, Session Handler & Upload controller
├── config.py                   # App Configuration (Secret keys, DB parameters, folder paths)
├── requirements.txt            # Project dependencies
├── schema.sql                  # MySQL database schema setup script
│
├── database/                   
│   ├── __init__.py
│   └── db.py                   # Database Access Layer: PyMySQL execution pool
│
├── models/                     # Data Models & Business Logic
│   ├── __init__.py
│   ├── auth.py                 # User signup, credentials validation, profile & password edits
│   ├── course.py               # Course catalogs, study materials, enrollment registries
│   ├── assignment.py           # Homework publishing, file uploads, submissions desk & marks
│   ├── notification.py         # Broadcast logs and alerts
│   └── ai_helper.py            # AI Study Companion core (Dual local/cloud engine)
│
├── static/                     # Frontend Assets
│   ├── css/
│   │   └── style.css           # Premium Indigo-Navy UI styles
│   ├── js/
│   │   └── main.js             # Collapsible sidebars, AJAX chat logs, alerts dismisser
│   └── uploads/                # Local File Repositories
│       ├── materials/          # Note storage
│       └── submissions/        # Student homework uploads
│
└── templates/                  # Frontend HTML Views (Jinja2)
    ├── base.html               # Main layout structure (Sidebars, flash messages)
    ├── login.html              # Modern glassmorphic login form
    ├── register.html           # Student self-registration form
    ├── admin/                  # Admin interfaces
    ├── faculty/                # Faculty interfaces
    └── student/                # Student interfaces
```

---

## Database Schema Structure

The database consists of **10 relational tables** with proper index definitions, primary keys, and foreign key relationships to prevent database anomalies:

1. **`admins`**: Administrator data registry.
2. **`faculty`**: Teacher accounts mapped by department.
3. **`students`**: Student directory with unique roll numbers.
4. **`courses`**: Active courses, linked to the `faculty` table via `faculty_id` (foreign key).
5. **`enrollments`**: Many-to-many relationship map between students and courses.
6. **`course_materials`**: Log of note paths linked to courses.
7. **`assignments`**: Assessment guidelines with specific due dates.
8. **`submissions`**: Homework uploads mapped to students and assignments.
9. **`marks`**: Evaluation scores and teacher feedback comments mapped to submissions.
10. **`notifications`**: Logs for events, filtered by role and recipient ID.

---

## Prerequisites & Setup

### Step 1: Install Python
Ensure Python 3.8 or above is installed on your local computer.

### Step 2: Set up MySQL Database
1. Run your MySQL server (via **XAMPP**, **WAMP**, or standard MySQL service).
2. Open your database manager (such as **phpMyAdmin** or MySQL command line).
3. Create a database named `lms_db` or let the script handle it:
   - Import the `schema.sql` file into your MySQL database server:
     ```sql
     source d:/LMS/schema.sql;
     ```

### Step 3: Install Dependencies
Open your command terminal (Command Prompt / Powershell / Git Bash) inside the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database Connections (Optional)
If your local MySQL uses a custom user or password, open `config.py` and modify the fields:
```python
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
```

---

## How to Run the Application

Start the Flask development server by running:
```bash
python app.py
```
Or:
```bash
flask run --port=5000
```

Open your browser and navigate to:
**`http://127.0.0.1:5000`**

---

## Default Login Credentials

Upon startup, the database auto-seeder automatically checks if there's any admin account. If empty, it creates:

- **Admin Account**:
  - **Email**: `admin@lms.com`
  - **Password**: `adminpassword`

- **Faculty & Students**:
  1. Login as Admin (`admin@lms.com` / `adminpassword`).
  2. Navigate to **Manage Faculty** -> Create a Faculty Account (e.g. `professor@lms.com` / `faculty123`).
  3. Navigate to **Manage Courses** -> Create a Course and assign it to the created Professor.
  4. Log out and navigate to **Register** to create a student account (e.g. `student@lms.com` / `student123`).
  5. Log in as Student -> browse available courses and enroll!

---

## AI Study Companion Details

The AI feature runs in **Dual Mode**:
- **Offline / Local Match Mode (Default)**: If no API key is specified, it uses pattern-matching (intents: `quiz`, `summarize`, `database`, `cloud`, `mvc`, `study tips`) to generate structured, formatted responses matching the chosen course details.
- **Online / Cloud Mode**: If you set the `GEMINI_API_KEY` environment variable, the system automatically uses Python's standard `urllib` library to make REST calls to Google's real `Gemini-1.5-flash` endpoint, giving you full conversational capability.
  - To enable, set the environment variable in your terminal before launching:
    ```cmd
    set GEMINI_API_KEY=your_actual_api_key_here
    ```

---

## Internship Viva Cheat Sheet

Be prepared to answer these common questions during your viva:

### Q1: Why did you choose `PyMySQL` instead of `mysqlclient`?
> **Answer**: `mysqlclient` requires a C-compiler wrapper to compile MySQL binaries during installation, which often causes compilation errors on Windows development machines. `PyMySQL` is a pure Python implementation of the MySQL client, which is 100% stable, easily installed via pip, and does not require C compilations.

### Q2: How does session management work in your app?
> **Answer**: Flask uses cryptographically signed client-side cookies. The session data is serialized and stored in the cookie. The `SECRET_KEY` in `config.py` is used to sign the cookie. If someone attempts to modify the cookie values in the browser, Flask detects the signature mismatch and invalidates the session, ensuring secure logins.

### Q3: What is password hashing, and why is it important?
> **Answer**: We never store passwords in plain text because if the database is compromised, all user accounts are exposed. Instead, we use `werkzeug.security` to hash the passwords using **PBKDF2 with SHA-256** salt encryption. When logging in, we hash the input and compare it to the stored hash using `check_password_hash`. It is mathematically infeasible to reverse a hashed password back to plain text.

### Q4: How is the database decoupled from routing?
> **Answer**: We use the MVC architecture. `app.py` handles controller tasks (handling HTTP requests, sessions, and uploads). `database/db.py` executes SQL queries. The folder `models/` contains separate business logic operations. For instance, `models/course.py` holds course SQL parameters, keeping `app.py` clean and easy to test or read.

### Q5: How are file uploads kept secure in your app?
> **Answer**:
> 1. **Allowed Extensions**: We restrict upload types to safe document or zip formats using the `allowed_file` check, preventing users from uploading executable `.exe` or script files.
> 2. **File Size Limit**: We limit sizes to 10MB using `MAX_CONTENT_LENGTH`.
> 3. **Unique Naming**: We pass filenames through `secure_filename` to sanitize special characters and prepend unique timestamps and IDs to prevent files from overwriting each other.


---

## License

This project is developed for educational purposes as part of a Cloud Computing course project.

