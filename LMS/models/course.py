from database.db import fetch_all, fetch_one, execute_query

# ==========================================
# ADMIN COURSE FUNCTIONS
# ==========================================

def create_course(name, code, description, faculty_id):
    """
    Creates a new course and assigns a faculty member.
    """
    query = """
        INSERT INTO courses (name, code, description, faculty_id)
        VALUES (%s, %s, %s, %s)
    """
    try:
        return execute_query(query, (name, code, description, faculty_id), return_lastrowid=True)
    except Exception as e:
        print(f"Error creating course: {e}")
        return None

def get_all_courses():
    """
    Returns all courses along with assigned faculty names.
    """
    query = """
        SELECT c.*, f.name as faculty_name, f.department as faculty_department
        FROM courses c
        LEFT JOIN faculty f ON c.faculty_id = f.id
        ORDER BY c.created_at DESC
    """
    return fetch_all(query)

def get_course_by_id(course_id):
    """
    Fetches a single course with assigned faculty.
    """
    query = """
        SELECT c.*, f.name as faculty_name, f.email as faculty_email, f.department as faculty_department
        FROM courses c
        LEFT JOIN faculty f ON c.faculty_id = f.id
        WHERE c.id = %s
    """
    return fetch_one(query, (course_id,))

def update_course(course_id, name, code, description, faculty_id):
    """
    Updates course details.
    """
    query = """
        UPDATE courses 
        SET name = %s, code = %s, description = %s, faculty_id = %s 
        WHERE id = %s
    """
    try:
        execute_query(query, (name, code, description, faculty_id if faculty_id else None, course_id))
        return True
    except Exception as e:
        print(f"Error updating course: {e}")
        return False

def delete_course(course_id):
    """
    Deletes a course. Foreign keys will cascade delete enrollments, assignments, etc.
    """
    query = "DELETE FROM courses WHERE id = %s"
    try:
        execute_query(query, (course_id,))
        return True
    except Exception as e:
        print(f"Error deleting course: {e}")
        return False


# ==========================================
# FACULTY COURSE FUNCTIONS
# ==========================================

def get_courses_by_faculty(faculty_id):
    """
    Returns courses assigned to a particular faculty.
    """
    query = "SELECT * FROM courses WHERE faculty_id = %s ORDER BY created_at DESC"
    return fetch_all(query, (faculty_id,))

def upload_material(course_id, title, description, file_path):
    """
    Uploads a study material note (PDF, DOCX) for a course.
    """
    query = """
        INSERT INTO course_materials (course_id, title, description, file_path)
        VALUES (%s, %s, %s, %s)
    """
    try:
        return execute_query(query, (course_id, title, description, file_path), return_lastrowid=True)
    except Exception as e:
        print(f"Error uploading material: {e}")
        return None

def get_materials_by_course(course_id):
    """
    Returns all materials uploaded for a specific course.
    """
    query = "SELECT * FROM course_materials WHERE course_id = %s ORDER BY uploaded_at DESC"
    return fetch_all(query, (course_id,))

def delete_material(material_id):
    """
    Deletes a course material note.
    """
    query = "DELETE FROM course_materials WHERE id = %s"
    try:
        execute_query(query, (material_id,))
        return True
    except Exception as e:
        print(f"Error deleting material: {e}")
        return False


# ==========================================
# STUDENT COURSE FUNCTIONS
# ==========================================

def get_enrolled_courses(student_id):
    """
    Returns all courses a student is enrolled in, along with faculty name.
    """
    query = """
        SELECT c.*, f.name as faculty_name, e.enrolled_at 
        FROM enrollments e
        JOIN courses c ON e.course_id = c.id
        LEFT JOIN faculty f ON c.faculty_id = f.id
        WHERE e.student_id = %s
        ORDER BY e.enrolled_at DESC
    """
    return fetch_all(query, (student_id,))

def get_available_courses(student_id):
    """
    Returns all courses a student is NOT currently enrolled in.
    """
    query = """
        SELECT c.*, f.name as faculty_name 
        FROM courses c
        LEFT JOIN faculty f ON c.faculty_id = f.id
        WHERE c.id NOT IN (
            SELECT course_id FROM enrollments WHERE student_id = %s
        )
        ORDER BY c.created_at DESC
    """
    return fetch_all(query, (student_id,))

def enroll_student_in_course(student_id, course_id):
    """
    Enrolls a student in a course.
    """
    query = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
    try:
        execute_query(query, (student_id, course_id))
        return True
    except Exception as e:
        print(f"Error enrolling student: {e}")
        return False

def unenroll_student_from_course(student_id, course_id):
    """
    Drops a student from a course.
    """
    query = "DELETE FROM enrollments WHERE student_id = %s AND course_id = %s"
    try:
        execute_query(query, (student_id, course_id))
        return True
    except Exception as e:
        print(f"Error unenrolling student: {e}")
        return False

def search_courses(query, student_id=None, enrolled=True):
    """
    Searches courses by code or name.
    If student_id is provided and enrolled=True, searches within enrolled courses.
    If enrolled=False, searches within available (not enrolled) courses.
    """
    like_query = f"%{query}%"
    if student_id:
        if enrolled:
            sql = """
                SELECT c.*, f.name as faculty_name 
                FROM enrollments e
                JOIN courses c ON e.course_id = c.id
                LEFT JOIN faculty f ON c.faculty_id = f.id
                WHERE e.student_id = %s AND (c.name LIKE %s OR c.code LIKE %s)
                ORDER BY c.name ASC
            """
            return fetch_all(sql, (student_id, like_query, like_query))
        else:
            sql = """
                SELECT c.*, f.name as faculty_name 
                FROM courses c
                LEFT JOIN faculty f ON c.faculty_id = f.id
                WHERE c.id NOT IN (
                    SELECT course_id FROM enrollments WHERE student_id = %s
                ) AND (c.name LIKE %s OR c.code LIKE %s)
                ORDER BY c.name ASC
            """
            return fetch_all(sql, (student_id, like_query, like_query))
    else:
        sql = """
            SELECT c.*, f.name as faculty_name 
            FROM courses c
            LEFT JOIN faculty f ON c.faculty_id = f.id
            WHERE c.name LIKE %s OR c.code LIKE %s
            ORDER BY c.name ASC
        """
        return fetch_all(sql, (like_query, like_query))
