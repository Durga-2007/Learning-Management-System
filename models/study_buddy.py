from database.db import fetch_all, fetch_one, execute_query

def get_student_course_stats(course_id):
    """
    Returns a list of students enrolled in the course along with their average scores.
    """
    query = """
        SELECT s.id as student_id, s.name, s.email, s.roll_no,
               COALESCE(AVG(m.score), 0) as average_score,
               COUNT(m.id) as graded_assignments
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        LEFT JOIN submissions sub ON sub.student_id = s.id AND sub.assignment_id IN (SELECT id FROM assignments WHERE course_id = %s)
        LEFT JOIN marks m ON m.submission_id = sub.id
        WHERE e.course_id = %s
        GROUP BY s.id
    """
    return fetch_all(query, (course_id, course_id))

def get_recommended_buddies(student_id, course_id):
    """
    Returns the top 3 recommended buddies for a specific student in a course.
    Logic:
    - If student average < 60, prioritize buddies with average > 80.
    - Otherwise, just recommend top performing students.
    - Exclude already paired buddies.
    """
    stats = get_student_course_stats(course_id)
    
    # Find current student's stats
    current_student = next((s for s in stats if s['student_id'] == student_id), None)
    
    if not current_student:
        return []

    my_score = current_student['average_score']
    
    # Get IDs of already paired buddies (either initiated by me or accepted by me)
    paired_query = """
        SELECT buddy_id as id FROM study_buddies WHERE student_id = %s AND course_id = %s
        UNION
        SELECT student_id as id FROM study_buddies WHERE buddy_id = %s AND course_id = %s
    """
    paired_records = fetch_all(paired_query, (student_id, course_id, student_id, course_id))
    paired_ids = [record['id'] for record in paired_records]
    
    potential_buddies = [
        s for s in stats 
        if s['student_id'] != student_id and s['student_id'] not in paired_ids
    ]
    
    # Sorting logic
    if my_score < 60:
        # Prioritize high performers (>80), then sort by highest score
        potential_buddies.sort(key=lambda x: (x['average_score'] > 80, x['average_score']), reverse=True)
    else:
        # Just sort by highest score to learn from the best
        potential_buddies.sort(key=lambda x: x['average_score'], reverse=True)
        
    return potential_buddies[:3]

def get_active_buddies(student_id):
    """
    Get the current student's active buddies across all courses.
    """
    query = """
        SELECT sb.*, c.name as course_name, 
               CASE 
                   WHEN sb.student_id = %s THEN b1.name 
                   ELSE b2.name 
               END as buddy_name,
               CASE 
                   WHEN sb.student_id = %s THEN b1.email 
                   ELSE b2.email 
               END as buddy_email
        FROM study_buddies sb
        JOIN courses c ON sb.course_id = c.id
        LEFT JOIN students b1 ON sb.buddy_id = b1.id
        LEFT JOIN students b2 ON sb.student_id = b2.id
        WHERE sb.student_id = %s OR sb.buddy_id = %s
        ORDER BY sb.created_at DESC
    """
    return fetch_all(query, (student_id, student_id, student_id, student_id))

def add_buddy(student_id, buddy_id, course_id):
    """
    Records a new study buddy pairing.
    """
    # Prevent duplicate pairs in reverse order
    check_query = """
        SELECT id FROM study_buddies 
        WHERE (student_id = %s AND buddy_id = %s AND course_id = %s)
           OR (student_id = %s AND buddy_id = %s AND course_id = %s)
    """
    existing = fetch_one(check_query, (student_id, buddy_id, course_id, buddy_id, student_id, course_id))
    if existing:
        return False
        
    query = """
        INSERT INTO study_buddies (student_id, buddy_id, course_id)
        VALUES (%s, %s, %s)
    """
    try:
        execute_query(query, (student_id, buddy_id, course_id))
        return True
    except Exception as e:
        print(f"Error adding buddy: {e}")
        return False

def get_faculty_buddy_stats(faculty_id):
    """
    Get buddy pairs for all courses taught by a specific faculty.
    """
    query = """
        SELECT sb.*, c.name as course_name, s1.name as student_name, s2.name as buddy_name
        FROM study_buddies sb
        JOIN courses c ON sb.course_id = c.id
        JOIN students s1 ON sb.student_id = s1.id
        JOIN students s2 ON sb.buddy_id = s2.id
        WHERE c.faculty_id = %s
        ORDER BY sb.created_at DESC
    """
    return fetch_all(query, (faculty_id,))

def get_admin_buddy_stats():
    """
    Get global stats for Admin Dashboard.
    Returns total matches and recent pairs.
    """
    total_query = "SELECT COUNT(*) as total FROM study_buddies"
    total_result = fetch_one(total_query)
    
    recent_query = """
        SELECT sb.*, c.name as course_name, s1.name as student_name, s2.name as buddy_name
        FROM study_buddies sb
        JOIN courses c ON sb.course_id = c.id
        JOIN students s1 ON sb.student_id = s1.id
        JOIN students s2 ON sb.buddy_id = s2.id
        ORDER BY sb.created_at DESC LIMIT 5
    """
    recent_pairs = fetch_all(recent_query)
    
    # Also calculate students needing support (average < 60 across any course)
    support_query = """
        SELECT COUNT(DISTINCT s.id) as total_needing_support
        FROM students s
        JOIN enrollments e ON s.id = e.student_id
        LEFT JOIN submissions sub ON sub.student_id = s.id AND sub.assignment_id IN (SELECT id FROM assignments WHERE course_id = e.course_id)
        LEFT JOIN marks m ON m.submission_id = sub.id
        GROUP BY e.student_id, e.course_id
        HAVING COALESCE(AVG(m.score), 0) < 60
    """
    # Sum up students needing support
    support_results = fetch_all(support_query)
    total_support = len(support_results)
    
    return {
        'total_matches': total_result['total'] if total_result else 0,
        'recent_pairs': recent_pairs,
        'students_needing_support': total_support
    }
