from database.db import execute_query
import re

with open('schema_rag.sql', 'r') as f:
    sql_content = f.read()

# Remove comments
sql_clean = re.sub(r'--.*', '', sql_content)
sql_clean = re.sub(r'/\*.*?\*/', '', sql_clean, flags=re.DOTALL)

# Split by ';' to get individual statements
statements = [s.strip() for s in sql_clean.split(';') if s.strip() and len(s.strip()) > 5]

print(f"Found {len(statements)} SQL statements\n")

for i, stmt in enumerate(statements, 1):
    try:
        execute_query(stmt)
        print(f"✅ [{i}/{len(statements)}] Created: {stmt.split()[0:5]}")
    except Exception as e:
        if "already exists" in str(e):
            print(f"⚠️  [{i}/{len(statements)}] Table already exists")
        else:
            print(f"❌ [{i}/{len(statements)}] Error: {str(e)[:100]}")

print("\n✅ RAG schema setup complete!")
