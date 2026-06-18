# Project Structure

```
LMS/
+-- app.py                  # Main Flask application
+-- config.py               # Configuration settings
+-- create_db.py            # Database setup script
+-- schema.sql              # Core database schema
+-- requirements.txt        # Python dependencies
+--
+-- models/                 # Backend logic
|   +-- ai_helper.py        # AI/Gemini integration
|   +-- assignment.py       # Assignment CRUD
|   +-- course.py           # Course management
|   +-- gamification.py     # XP, streaks, badges
|   +-- study_buddy.py      # Smart buddy matching
|   +-- auth.py             # Authentication
|   +-- notification.py     # Notifications
|
+-- database/               # Database connection
|   +-- db.py               # PyMySQL connection pool
|
+-- templates/              # Jinja2 HTML templates
|   +-- base.html           # Base layout
|   +-- admin/              # Admin panel views
|   +-- faculty/            # Faculty views
|   +-- student/            # Student views
|
+-- static/                 # Frontend assets
    +-- css/style.css       # Custom stylesheet
    +-- js/                 # JavaScript modules
```
