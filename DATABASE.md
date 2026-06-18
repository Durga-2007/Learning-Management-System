# Database Schema Documentation

## Core Tables

| Table | Purpose |
|-------|---------|
| admins | Administrator accounts |
| faculty | Faculty/instructor accounts |
| students | Student accounts |
| courses | Course catalog |
| enrollments | Student-course mappings |
| course_materials | Uploaded study materials |
| assignments | Course assignments |
| submissions | Student assignment submissions |
| marks | Grading and feedback |

## Gamification Tables

| Table | Purpose |
|-------|---------|
| student_gamification | XP, streaks, and progression |
| xp_points | XP transaction log |
| badges | Available badge definitions |
| student_badges | Earned badge records |
| course_levels | Progressive course levels |
| daily_challenges | AI-generated quiz questions |
| challenge_results | Student quiz results |

## Setup

Run the schema setup:
```bash
python create_db.py
```
