import os
from database.db import fetch_one
from models import rag_helper

material_id = 4
material = fetch_one('SELECT * FROM course_materials WHERE id = %s', (material_id,))
print('material:', material)
if material:
    local_path = os.path.join('uploads', 'materials', material['file_path'])
    print('file exists:', os.path.exists(local_path), os.path.abspath(local_path))
    if os.path.exists(local_path):
        result = rag_helper.process_course_material(material_id, material['course_id'], local_path, material['title'])
        print('process result:', result)
    else:
        print('Missing file at path:', local_path)
else:
    print('No material found with id', material_id)
