# PowerShell script to create ~50 granular commits for GitHub contribution graph
# Each commit adds a logical piece of the LMS project

$ErrorActionPreference = "Continue"

# Commit 1: Project initialization
git add .gitignore
git commit -m "chore: initialize project with .gitignore"

# Commit 2: README
git add README.md
git commit -m "docs: add project README with feature overview"

# Commit 3: Requirements
git add requirements.txt
git commit -m "chore: add Python dependencies (Flask, PyMySQL, Werkzeug)"

# Commit 4: RAG requirements
git add requirements_rag.txt
git commit -m "chore: add RAG system dependencies"

# Commit 5: Config
git add config.py
git commit -m "feat: add application configuration module"

# Commit 6: Database schema
git add schema.sql
git commit -m "feat: add core database schema (users, courses, enrollments)"

# Commit 7: AI chat schema
git add schema_ai_chat.sql
git commit -m "feat: add AI chatbot conversation schema"

# Commit 8: RAG schema
git add schema_rag.sql
git commit -m "feat: add RAG vector storage schema"

# Commit 9: DB setup script
git add create_db.py
git commit -m "feat: add database initialization and seeding script"

# Commit 10: RAG setup
git add setup_rag_schema.py
git commit -m "feat: add RAG schema setup utility"

# Commit 11: Course model
git add models/course.py
git commit -m "feat(models): implement course CRUD operations"

# Commit 12: Assignment model
git add models/assignment.py
git commit -m "feat(models): implement assignment management model"

# Commit 13: AI helper base
git add models/ai_helper.py
git commit -m "feat(models): add AI helper with knowledge base and Gemini integration"

# Commit 14: Study buddy model
git add models/study_buddy.py
git commit -m "feat(models): implement study buddy matching algorithm"

# Commit 15: Gamification model
git add models/gamification.py
git commit -m "feat(models): add gamification engine (XP, streaks, badges, levels)"

# Commit 16: RAG engine
if (Test-Path "models/rag_engine.py") {
    git add models/rag_engine.py
    git commit -m "feat(models): implement RAG retrieval-augmented generation engine"
}

# Commit 17: Models init
if (Test-Path "models/__init__.py") {
    git add models/__init__.py
    git commit -m "chore(models): add models package init"
}

# Commit 18: CSS stylesheet
git add static/css/style.css
git commit -m "feat(ui): add custom CSS with design system and gamification styles"

# Commit 19: JS files
git add static/js/
git commit -m "feat(ui): add client-side JavaScript modules"

# Commit 20: Static assets (images, fonts etc)
git add static/
git commit -m "feat(ui): add remaining static assets and upload directories"

# Commit 21: Base template
git add templates/base.html
git commit -m "feat(templates): create base layout with sidebar, navbar, and gamification stats"

# Commit 22: Login template
git add templates/login.html
git commit -m "feat(templates): add login page template"

# Commit 23: Register template
if (Test-Path "templates/register.html") {
    git add templates/register.html
    git commit -m "feat(templates): add user registration template"
}

# Commit 24: Admin dashboard
if (Test-Path "templates/admin/dashboard.html") {
    git add templates/admin/dashboard.html
    git commit -m "feat(templates): add admin dashboard with analytics"
}

# Commit 25: Admin manage users
if (Test-Path "templates/admin/manage_faculty.html") {
    git add templates/admin/manage_faculty.html
    git commit -m "feat(templates): add admin faculty management view"
}

# Commit 26: Admin manage students
if (Test-Path "templates/admin/manage_students.html") {
    git add templates/admin/manage_students.html
    git commit -m "feat(templates): add admin student management view"
}

# Commit 27: Admin manage courses
if (Test-Path "templates/admin/manage_courses.html") {
    git add templates/admin/manage_courses.html
    git commit -m "feat(templates): add admin course management view"
}

# Commit 28: Remaining admin templates
git add templates/admin/
git commit -m "feat(templates): add remaining admin panel templates"

# Commit 29: Faculty dashboard
if (Test-Path "templates/faculty/dashboard.html") {
    git add templates/faculty/dashboard.html
    git commit -m "feat(templates): add faculty dashboard template"
}

# Commit 30: Faculty course detail
if (Test-Path "templates/faculty/course_detail.html") {
    git add templates/faculty/course_detail.html
    git commit -m "feat(templates): add faculty course detail and materials view"
}

# Commit 31: Faculty grade
if (Test-Path "templates/faculty/grade_submission.html") {
    git add templates/faculty/grade_submission.html
    git commit -m "feat(templates): add faculty grading interface"
}

# Commit 32: Remaining faculty templates
git add templates/faculty/
git commit -m "feat(templates): add remaining faculty templates"

# Commit 33: Student dashboard
git add templates/student/dashboard.html
git commit -m "feat(templates): add student dashboard with enrolled courses"

# Commit 34: Student course detail
git add templates/student/course_detail.html
git commit -m "feat(templates): add student course detail with Learning Game tab"

# Commit 35: Student profile
git add templates/student/profile.html
git commit -m "feat(templates): add student profile page"

# Commit 36: Student assignment submission
git add templates/student/submit_assignment.html
git commit -m "feat(templates): add assignment submission interface"

# Commit 37: Student AI assistant
git add templates/student/ai_assistant.html
git commit -m "feat(templates): add AI course assistant chat interface"

# Commit 38: Student study buddies
git add templates/student/study_buddies.html
git commit -m "feat(templates): add study buddy matcher and recommendations"

# Commit 39: Adventure path template
git add templates/student/adventure.html
git commit -m "feat(templates): add Duolingo-style learning adventure path"

# Commit 40: Play quiz template
git add templates/student/play_quiz.html
git commit -m "feat(templates): add interactive quiz player with progress tracking"

# Commit 41: Quiz results template
git add templates/student/quiz_results.html
git commit -m "feat(templates): add quiz results with retry/pass flow"

# Commit 42: Leaderboard template
git add templates/student/leaderboard.html
git commit -m "feat(templates): add global XP leaderboard with podium design"

# Commit 43: Remaining student templates
git add templates/student/
git commit -m "feat(templates): add remaining student templates"

# Commit 44: Remaining templates
git add templates/
git commit -m "feat(templates): add any remaining template files"

# Commit 45: Main application - auth routes
git add app.py
git commit -m "feat(app): implement Flask app with auth, admin, faculty, student routes"

# Commit 46: RAG implementation guide
git add RAG_IMPLEMENTATION_GUIDE.md
git commit -m "docs: add RAG implementation architecture guide"

# Commit 47: RAG summary
git add RAG_IMPLEMENTATION_SUMMARY.md
git commit -m "docs: add RAG implementation summary document"

# Commit 48: RAG quick start
git add RAG_QUICK_START.md
git commit -m "docs: add RAG quick start setup guide"

# Commit 49: RAG checklist
git add RAG_SETUP_CHECKLIST.md
git commit -m "docs: add RAG setup verification checklist"

# Commit 50: Debug and test utilities
git add debug_process_material.py
git add debug_rag_db.py
git add inspect_course_materials.py
git add inspect_env.py
git add test_rag_system.py
git commit -m "test: add debug scripts and RAG system test suite"

# Commit 51: Any remaining files
git add -A
git commit -m "chore: add any remaining project files"

# Rename branch to main
git branch -M main

Write-Host ""
Write-Host "=== All commits created! ==="
git log --oneline | Select-Object -First 55
Write-Host ""
Write-Host "Total commits:"
git rev-list --count HEAD
