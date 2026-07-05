from database.db import fetch_all, fetch_one, execute_query

# ==========================================
# FACULTY ASSIGNMENT FUNCTIONS
# ==========================================

def create_assignment(course_id, title, description, due_date):
    """
    Creates a new assignment for a course.
    """
    query = """
        INSERT INTO assignments (course_id, title, description, due_date)
        VALUES (%s, %s, %s, %s)
    """
    try:
        return execute_query(query, (course_id, title, description, due_date), return_lastrowid=True)
    except Exception as e:
        print(f"Error creating assignment: {e}")
        return None

def get_assignments_by_course(course_id):
    """
    Retrieves all assignments for a course, ordered by due date.
    """
    query = "SELECT * FROM assignments WHERE course_id = %s ORDER BY due_date ASC"
    return fetch_all(query, (course_id,))

def get_assignment_by_id(assignment_id):
    """
    Retrieves a single assignment by its ID.
    """
    query = """
        SELECT a.*, c.name as course_name, c.code as course_code
        FROM assignments a
        JOIN courses c ON a.course_id = c.id
        WHERE a.id = %s
    """
    return fetch_one(query, (assignment_id,))

def delete_assignment(assignment_id):
    """
    Deletes an assignment. Foreign keys will cascade delete submissions and marks.
    """
    query = "DELETE FROM assignments WHERE id = %s"
    try:
        execute_query(query, (assignment_id,))
        return True
    except Exception as e:
        print(f"Error deleting assignment: {e}")
        return False

def get_submissions_by_assignment(assignment_id):
    """
    Retrieves all student submissions for an assignment.
    """
    query = """
        SELECT s.*, st.name as student_name, st.roll_no as student_roll_no, m.score, m.feedback
        FROM submissions s
        JOIN students st ON s.student_id = st.id
        LEFT JOIN marks m ON s.id = m.submission_id
        WHERE s.assignment_id = %s
        ORDER BY s.submitted_at DESC
    """
    return fetch_all(query, (assignment_id,))

def get_submission_by_id(submission_id):
    """
    Retrieves details of a single submission.
    """
    query = """
        SELECT s.*, a.course_id, st.name as student_name, st.roll_no as student_roll_no, st.email as student_email,
               a.title as assignment_title, a.due_date, c.name as course_name, m.score, m.feedback
        FROM submissions s
        JOIN students st ON s.student_id = st.id
        JOIN assignments a ON s.assignment_id = a.id
        JOIN courses c ON a.course_id = c.id
        LEFT JOIN marks m ON s.id = m.submission_id
        WHERE s.id = %s
    """
    return fetch_one(query, (submission_id,))

def grade_submission(submission_id, score, feedback, graded_by):
    """
    Grades a submission. Inserts or updates the marks table and sets submission status to 'Graded'.
    """
    # Check if marks already exist for this submission
    existing_mark = fetch_one("SELECT id FROM marks WHERE submission_id = %s", (submission_id,))
    
    try:
        if existing_mark:
            # Update existing mark
            update_query = """
                UPDATE marks 
                SET score = %s, feedback = %s, graded_by = %s, graded_at = CURRENT_TIMESTAMP
                WHERE submission_id = %s
            """
            execute_query(update_query, (score, feedback, graded_by, submission_id))
        else:
            # Insert new mark
            insert_query = """
                INSERT INTO marks (submission_id, score, feedback, graded_by)
                VALUES (%s, %s, %s, %s)
            """
            execute_query(insert_query, (submission_id, score, feedback, graded_by))
        
        # Update submission status
        execute_query("UPDATE submissions SET status = 'Graded' WHERE id = %s", (submission_id,))
        return True
    except Exception as e:
        print(f"Error grading submission: {e}")
        return False


# ==========================================
# STUDENT ASSIGNMENT FUNCTIONS
# ==========================================

def get_student_submission(assignment_id, student_id):
    """
    Retrieves a student's submission for a particular assignment.
    """
    query = """
        SELECT s.*, m.score, m.feedback, f.name as graded_by_name
        FROM submissions s
        LEFT JOIN marks m ON s.id = m.submission_id
        LEFT JOIN faculty f ON m.graded_by = f.id
        WHERE s.assignment_id = %s AND s.student_id = %s
    """
    return fetch_one(query, (assignment_id, student_id))

def submit_assignment(assignment_id, student_id, file_path):
    """
    Submits an assignment. If already submitted, updates the submission file.
    """
    existing_submission = get_student_submission(assignment_id, student_id)
    
    try:
        if existing_submission:
            # If submission exists and is not graded, let's overwrite it
            if existing_submission['status'] == 'Submitted':
                update_query = """
                    UPDATE submissions 
                    SET file_path = %s, submitted_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """
                execute_query(update_query, (file_path, existing_submission['id']))
                return existing_submission['id']
            else:
                # Already graded - do not allow resubmission (or handle as business logic)
                return None
        else:
            # Insert new submission
            insert_query = """
                INSERT INTO submissions (assignment_id, student_id, file_path, status)
                VALUES (%s, %s, %s, 'Submitted')
            """
            return execute_query(insert_query, (assignment_id, student_id, file_path), return_lastrowid=True)
    except Exception as e:
        print(f"Error submitting assignment: {e}")
        return None

def get_student_grades_by_course(student_id, course_id):
    """
    Retrieves all assignments for a course along with student's submissions and grades.
    """
    query = """
        SELECT a.id as assignment_id, a.title, a.description, a.due_date,
               s.id as submission_id, s.file_path, s.submitted_at, s.status,
               m.score, m.feedback, f.name as graded_by_name
        FROM assignments a
        LEFT JOIN submissions s ON a.id = s.assignment_id AND s.student_id = %s
        LEFT JOIN marks m ON s.id = m.submission_id
        LEFT JOIN faculty f ON m.graded_by = f.id
        WHERE a.course_id = %s
        ORDER BY a.due_date ASC
    """
    return fetch_all(query, (student_id, course_id))

def get_all_student_grades(student_id):
    """
    Retrieves all graded submissions for a student across all courses.
    """
    query = """
        SELECT s.id as submission_id, s.submitted_at, a.title as assignment_title, 
               c.name as course_name, c.code as course_code, m.score, m.feedback, f.name as graded_by_name
        FROM submissions s
        JOIN assignments a ON s.assignment_id = a.id
        JOIN courses c ON a.course_id = c.id
        JOIN marks m ON s.id = m.submission_id
        LEFT JOIN faculty f ON m.graded_by = f.id
        WHERE s.student_id = %s
        ORDER BY m.graded_at DESC
    """
    return fetch_all(query, (student_id,))
