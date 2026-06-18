from werkzeug.security import generate_password_hash, check_password_hash
from database.db import fetch_one, execute_query

def register_student(name, email, password, roll_no, department):
    """
    Registers a new student. Hashes the password before storing.
    """
    password_hash = generate_password_hash(password)
    query = """
        INSERT INTO students (name, email, password_hash, roll_no, department)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        student_id = execute_query(query, (name, email, password_hash, roll_no, department), return_lastrowid=True)
        return student_id
    except Exception as e:
        print(f"Error registering student: {e}")
        return None

def register_faculty(name, email, password, department):
    """
    Registers a new faculty member. Hashes the password before storing.
    """
    password_hash = generate_password_hash(password)
    query = """
        INSERT INTO faculty (name, email, password_hash, department)
        VALUES (%s, %s, %s, %s)
    """
    try:
        faculty_id = execute_query(query, (name, email, password_hash, department), return_lastrowid=True)
        return faculty_id
    except Exception as e:
        print(f"Error registering faculty: {e}")
        return None

def register_admin(name, email, password):
    """
    Registers a new admin. Hashes the password before storing.
    """
    password_hash = generate_password_hash(password)
    query = """
        INSERT INTO admins (name, email, password_hash)
        VALUES (%s, %s, %s)
    """
    try:
        admin_id = execute_query(query, (name, email, password_hash), return_lastrowid=True)
        return admin_id
    except Exception as e:
        print(f"Error registering admin: {e}")
        return None

def verify_login(email, password, role):
    """
    Verifies user login based on role.
    Returns user details (excluding password_hash) if successful, otherwise None.
    """
    table = ""
    if role == 'student':
        table = 'students'
    elif role == 'faculty':
        table = 'faculty'
    elif role == 'admin':
        table = 'admins'
    else:
        return None

    query = f"SELECT * FROM {table} WHERE email = %s"
    user = fetch_one(query, (email,))
    
    if user and check_password_hash(user['password_hash'], password):
        # Remove hash from dict before returning for security
        user.pop('password_hash', None)
        return user
    return None

def get_user_by_id(user_id, role):
    """
    Fetches user data by ID and role.
    """
    table = ""
    if role == 'student':
        table = 'students'
    elif role == 'faculty':
        table = 'faculty'
    elif role == 'admin':
        table = 'admins'
    else:
        return None

    query = f"SELECT * FROM {table} WHERE id = %s"
    user = fetch_one(query, (user_id,))
    if user:
        user.pop('password_hash', None)
    return user

def change_password(user_id, role, current_password, new_password):
    """
    Changes a user's password after verifying their current password.
    """
    table = ""
    if role == 'student':
        table = 'students'
    elif role == 'faculty':
        table = 'faculty'
    elif role == 'admin':
        table = 'admins'
    else:
        return False

    query = f"SELECT password_hash FROM {table} WHERE id = %s"
    user = fetch_one(query, (user_id,))
    
    if user and check_password_hash(user['password_hash'], current_password):
        new_hash = generate_password_hash(new_password)
        update_query = f"UPDATE {table} SET password_hash = %s WHERE id = %s"
        execute_query(update_query, (new_hash, user_id))
        return True
    return False

def update_profile(user_id, role, name, email, department=None, roll_no=None):
    """
    Updates basic profile details of a user.
    """
    if role == 'student':
        query = """
            UPDATE students 
            SET name = %s, email = %s, roll_no = %s, department = %s 
            WHERE id = %s
        """
        params = (name, email, roll_no, department, user_id)
    elif role == 'faculty':
        query = """
            UPDATE faculty 
            SET name = %s, email = %s, department = %s 
            WHERE id = %s
        """
        params = (name, email, department, user_id)
    elif role == 'admin':
        query = """
            UPDATE admins 
            SET name = %s, email = %s 
            WHERE id = %s
        """
        params = (name, email, user_id)
    else:
        return False

    try:
        execute_query(query, params)
        return True
    except Exception as e:
        print(f"Error updating profile: {e}")
        return False
