from database.db import fetch_all, fetch_one, execute_query
from datetime import datetime, timedelta
import models.ai_helper as ai_model

def init_student_profile(student_id):
    """Ensures a gamification profile exists for the student."""
    query = "SELECT id FROM student_gamification WHERE student_id = %s"
    if not fetch_one(query, (student_id,)):
        execute_query(
            "INSERT INTO student_gamification (student_id, total_xp, current_streak, longest_streak) VALUES (%s, 0, 0, 0)",
            (student_id,)
        )

def check_and_reset_streak(student_id):
    """
    Called on page request.
    Resets current_streak to 0 if the student missed yesterday.
    Does NOT increment the streak.
    """
    init_student_profile(student_id)
    profile = fetch_one("SELECT * FROM student_gamification WHERE student_id = %s", (student_id,))
    if not profile:
        return
        
    today = datetime.now().date()
    last_active = profile['last_active_date']
    
    if last_active and last_active < today - timedelta(days=1):
        # Missed a day, reset streak to 0
        execute_query(
            "UPDATE student_gamification SET current_streak = 0 WHERE student_id = %s",
            (student_id,)
        )

def increment_daily_streak(student_id):
    """
    Called only when a student successfully passes a level quiz (4/5 or 5/5).
    Increments their daily streak.
    Returns (incremented: bool, current_streak: int).
    """
    init_student_profile(student_id)
    profile = fetch_one("SELECT * FROM student_gamification WHERE student_id = %s", (student_id,))
    if not profile:
        return False, 0
        
    today = datetime.now().date()
    last_active = profile['last_active_date']
    current_streak = profile['current_streak']
    longest_streak = profile['longest_streak']
    incremented = False
    
    if not last_active:
        current_streak = 1
        incremented = True
    elif last_active == today:
        # Already passed a quiz today, do not double-increment
        incremented = False
    elif last_active == today - timedelta(days=1):
        # Passed a quiz yesterday, increment streak
        current_streak += 1
        incremented = True
    else:
        # Missed days, start new streak from 1
        current_streak = 1
        incremented = True
        
    if current_streak > longest_streak:
        longest_streak = current_streak
        
    if incremented:
        execute_query(
            "UPDATE student_gamification SET current_streak = %s, longest_streak = %s, last_active_date = %s WHERE student_id = %s",
            (current_streak, longest_streak, today, student_id)
        )
        # Check if they earned a streak badge
        check_and_award_badges(student_id)
    else:
        current_streak = profile['current_streak']
    
    return incremented, current_streak

def award_xp(student_id, amount):
    """Adds XP to the student's profile."""
    init_student_profile(student_id)
    execute_query(
        "UPDATE student_gamification SET total_xp = total_xp + %s WHERE student_id = %s",
        (amount, student_id)
    )

def check_and_award_badges(student_id):
    """Evaluates and awards badges based on streaks, scores, etc."""
    profile = fetch_one("SELECT * FROM student_gamification WHERE student_id = %s", (student_id,))
    if not profile:
        return
        
    badges = fetch_all("SELECT * FROM badges")
    earned = fetch_all("SELECT badge_id FROM student_badges WHERE student_id = %s", (student_id,))
    earned_ids = [b['badge_id'] for b in earned]
    
    for badge in badges:
        if badge['id'] in earned_ids:
            continue
            
        req_type = badge['requirement_type']
        req_val = badge['requirement_value']
        should_award = False
        
        if req_type == 'streak' and profile['current_streak'] >= req_val:
            should_award = True
        elif req_type == 'score':
            # Check average quiz score
            avg_score = fetch_one("SELECT AVG(score) as avg FROM challenge_results WHERE student_id = %s", (student_id,))
            if avg_score and avg_score['avg'] is not None and avg_score['avg'] >= req_val:
                should_award = True
        elif req_type == 'completion':
            # Course champion logic could be here
            pass
            
        if should_award:
            execute_query(
                "INSERT INTO student_badges (student_id, badge_id) VALUES (%s, %s)",
                (student_id, badge['id'])
            )

def get_student_stats(student_id):
    """Returns XP, Streaks, and Earned Badges."""
    init_student_profile(student_id)
    profile = fetch_one("SELECT * FROM student_gamification WHERE student_id = %s", (student_id,))
    
    badges_query = """
        SELECT b.*, sb.earned_at 
        FROM badges b 
        JOIN student_badges sb ON b.id = sb.badge_id 
        WHERE sb.student_id = %s
        ORDER BY sb.earned_at DESC
    """
    profile['earned_badges'] = fetch_all(badges_query, (student_id,))
    return profile

def get_leaderboard():
    """Returns top 10 students by XP and Streaks."""
    query = """
        SELECT s.name, sg.total_xp, sg.current_streak, sg.longest_streak
        FROM student_gamification sg
        JOIN students s ON sg.student_id = s.id
        ORDER BY sg.total_xp DESC, sg.current_streak DESC
        LIMIT 10
    """
    return fetch_all(query)

def get_or_generate_course_levels(course_id, course_description):
    """
    Returns the levels for a course. If none exist, it invents 5 default ones.
    In a fully automated system, AI could generate these names based on description.
    For now, we use a structured fallback to ensure levels exist.
    """
    levels = fetch_all("SELECT * FROM course_levels WHERE course_id = %s ORDER BY level_number ASC", (course_id,))
    if not levels:
        # Auto-generate 5 levels
        level_names = [
            "Fundamentals & Basics",
            "Core Concepts",
            "Intermediate Applications",
            "Advanced Techniques",
            "Mastery & Optimization"
        ]
        for i, name in enumerate(level_names):
            execute_query(
                "INSERT INTO course_levels (course_id, level_number, title, description) VALUES (%s, %s, %s, %s)",
                (course_id, i+1, name, f"Master the {name.lower()} of this course.")
            )
        levels = fetch_all("SELECT * FROM course_levels WHERE course_id = %s ORDER BY level_number ASC", (course_id,))
    return levels

def get_adventure_path(student_id):
    """
    Builds the Duolingo-style path for the student.
    Fetches enrolled courses, their levels, and which levels are unlocked.
    Level N is unlocked if Level N-1 has a passed challenge result.
    """
    courses_query = """
        SELECT c.* 
        FROM courses c 
        JOIN enrollments e ON c.id = e.course_id 
        WHERE e.student_id = %s
    """
    courses = fetch_all(courses_query, (student_id,))
    
    adventure = []
    for c in courses:
        levels = get_or_generate_course_levels(c['id'], c['description'])
        
        # Check which ones are passed
        passed_query = "SELECT level_id FROM challenge_results WHERE student_id = %s AND passed = TRUE"
        passed_results = fetch_all(passed_query, (student_id,))
        passed_ids = [r['level_id'] for r in passed_results]
        
        path = []
        is_unlocked = True # Level 1 is always unlocked
        for lvl in levels:
            lvl['is_passed'] = lvl['id'] in passed_ids
            lvl['is_unlocked'] = is_unlocked
            
            # The next level is unlocked only if this one is passed
            if not lvl['is_passed']:
                is_unlocked = False
                
            path.append(lvl)
            
        c['levels'] = path
        adventure.append(c)
        
    return adventure

def generate_and_save_quiz(level_id, course_context):
    """Generates exactly 5 course-specific questions for the level and saves them to DB."""
    mcqs = ai_model.generate_level_quiz_json(course_context)
    if not mcqs or len(mcqs) < 5:
        mcqs = ai_model.get_topic_fallback_quiz(course_context)
    if not mcqs:
        return False

    mcqs = mcqs[:5]
        
    execute_query("DELETE FROM daily_challenges WHERE level_id = %s", (level_id,))
    
    for q in mcqs:
        execute_query(
            "INSERT INTO daily_challenges (level_id, question, option_a, option_b, option_c, option_d, correct_option, explanation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (level_id, q['question'], q['A'], q['B'], q['C'], q['D'], q['correct'], q['explanation'])
        )
    return True

def get_quiz_for_level(level_id, course_context):
    """Fetches exactly 5 questions for a level. Regenerates if missing or incomplete."""
    questions = fetch_all("SELECT * FROM daily_challenges WHERE level_id = %s", (level_id,))
    if len(questions) != 5:
        generate_and_save_quiz(level_id, course_context)
        questions = fetch_all("SELECT * FROM daily_challenges WHERE level_id = %s", (level_id,))
    return questions
