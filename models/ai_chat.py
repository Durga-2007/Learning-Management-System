from database.db import fetch_all, fetch_one, execute_query


def create_chat_session(student_id, course_id, title, last_message):
    query = """
        INSERT INTO ai_chats (student_id, course_id, title, last_message, created_at, updated_at)
        VALUES (%s, %s, %s, %s, NOW(), NOW())
    """
    return execute_query(query, (student_id, course_id, title, last_message), return_lastrowid=True)


def update_chat_last_message(chat_id, last_message):
    query = """
        UPDATE ai_chats
        SET last_message = %s,
            updated_at = NOW()
        WHERE id = %s
    """
    return execute_query(query, (last_message, chat_id))


def get_chat_sessions(student_id, course_id=None):
    query = """
        SELECT c.id,
               c.title,
               c.last_message,
               c.updated_at,
               c.course_id,
               COUNT(m.id) AS message_count
        FROM ai_chats c
        LEFT JOIN ai_messages m ON m.chat_id = c.id
        WHERE c.student_id = %s
    """
    params = [student_id]
    if course_id:
        query += " AND c.course_id = %s"
        params.append(course_id)
    query += " GROUP BY c.id ORDER BY c.updated_at DESC"
    return fetch_all(query, tuple(params))


def get_chat_session(student_id, course_id, chat_id):
    query = """
        SELECT * FROM ai_chats
        WHERE id = %s AND student_id = %s AND course_id = %s
    """
    return fetch_one(query, (chat_id, student_id, course_id))


def get_recent_messages(chat_id, limit=8):
    query = """
        SELECT id, sender, content, created_at
        FROM ai_messages
        WHERE chat_id = %s
        ORDER BY created_at DESC
        LIMIT %s
    """
    return fetch_all(query, (chat_id, limit))


def get_chat_messages(chat_id):
    query = """
        SELECT id, sender, content, created_at
        FROM ai_messages
        WHERE chat_id = %s
        ORDER BY created_at ASC
    """
    return fetch_all(query, (chat_id,))


def create_chat_message(chat_id, sender, content):
    query = """
        INSERT INTO ai_messages (chat_id, sender, content, created_at)
        VALUES (%s, %s, %s, NOW())
    """
    return execute_query(query, (chat_id, sender, content), return_lastrowid=True)


def log_usage(student_id, course_id, chat_id, event_type, details=None):
    query = """
        INSERT INTO ai_usage_logs (student_id, course_id, chat_id, event_type, details, created_at)
        VALUES (%s, %s, %s, %s, %s, NOW())
    """
    return execute_query(query, (student_id, course_id, chat_id, event_type, details))


def get_course_usage_summary(course_id):
    query = """
        SELECT
            COUNT(DISTINCT c.id) AS total_conversations,
            COUNT(m.id) AS total_messages,
            COUNT(DISTINCT c.student_id) AS active_students,
            IFNULL(ROUND(COUNT(m.id) / NULLIF(COUNT(DISTINCT c.id), 0), 1), 0) AS avg_messages_per_conversation
        FROM ai_chats c
        LEFT JOIN ai_messages m ON m.chat_id = c.id
        WHERE c.course_id = %s
    """
    return fetch_one(query, (course_id,))
