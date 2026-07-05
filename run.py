print("STEP 1")

from app import app

print("STEP 2")

from waitress import serve

print("STEP 3")

serve(app, host="127.0.0.1", port=8000)