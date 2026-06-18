from database.db import fetch_all, fetch_one, execute_query

def create_notification(user_role, user_id, message):
    """
    Creates a new notification entry.
    - user_role: 'student', 'faculty', 'admin', or 'all'
    - user_id: ID of the specific user (if NULL/None, the notification goes to all users of that role)
    - message: The notification message text
    """
    query = """
        INSERT INTO notifications (user_role, user_id, message)
        VALUES (%s, %s, %s)
    """
    try:
        return execute_query(query, (user_role, user_id, message), return_lastrowid=True)
    except Exception as e:
        print(f"Error creating notification: {e}")
        return None

def get_notifications(user_role, user_id, limit=20):
    """
    Fetches notifications for a user based on their role and specific ID.
    Includes notifications targeted to their role globally (user_id IS NULL)
    or to their specific ID.
    """
    query = """
        SELECT * FROM notifications
        WHERE (user_role = %s AND (user_id = %s OR user_id IS NULL))
           OR (user_role = 'all')
        ORDER BY created_at DESC
        LIMIT %s
    """
    return fetch_all(query, (user_role, user_id, limit))

def get_unread_count(user_role, user_id):
    """
    Returns the count of unread notifications for a user.
    """
    query = """
        SELECT COUNT(*) as unread_count FROM notifications
        WHERE ((user_role = %s AND (user_id = %s OR user_id IS NULL))
           OR (user_role = 'all'))
          AND is_read = FALSE
    """
    result = fetch_one(query, (user_role, user_id))
    return result['unread_count'] if result else 0

def mark_all_as_read(user_role, user_id):
    """
    Marks all notifications for a specific user as read.
    """
    query = """
        UPDATE notifications
        SET is_read = TRUE
        WHERE (user_role = %s AND (user_id = %s OR user_id IS NULL))
           OR (user_role = 'all')
    """
    try:
        execute_query(query, (user_role, user_id))
        return True
    except Exception as e:
        print(f"Error marking notifications as read: {e}")
        return False
