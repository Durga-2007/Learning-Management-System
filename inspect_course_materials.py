from database.db import fetch_all

print('course_materials columns:')
cols = fetch_all('SHOW COLUMNS FROM course_materials')
for c in cols:
    print(c)

print('\nExample rows:')
rows = fetch_all('SELECT * FROM course_materials LIMIT 3')
for r in rows:
    print(r)
