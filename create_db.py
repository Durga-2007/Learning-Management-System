import pymysql
from config import Config

def init_database():
    print("Connecting to MySQL server...")
    try:
        # Connect to MySQL Server (without specifying database name first)
        connection = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            autocommit=True
        )
        
        with connection.cursor() as cursor:
            # 1. Create the database
            print("Creating database 'lms_db' if it doesn't exist...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS lms_db")
            
            # 2. Select the database
            cursor.execute("USE lms_db")
            print("Connected to database 'lms_db'. Starting schema import...")
            
            # 3. Read and execute schema.sql
            with open("schema.sql", "r") as schema_file:
                schema_sql = schema_file.read()
                
            # Split queries by semicolon to execute them one by one
            queries = schema_sql.split(";")
            query_count = 0
            
            for query in queries:
                # Remove leading/trailing whitespace
                cleaned_query = query.strip()
                # Remove comment lines from the beginning of the query
                lines = cleaned_query.split('\n')
                non_comment_lines = [l for l in lines if not l.strip().startswith('--') and l.strip()]
                cleaned_query = '\n'.join(non_comment_lines).strip()
                
                # Skip empty, USE, and CREATE DATABASE statements (already handled above)
                if not cleaned_query:
                    continue
                upper_query = cleaned_query.upper()
                if upper_query.startswith("USE ") or upper_query.startswith("CREATE DATABASE"):
                    continue
                    
                cursor.execute(cleaned_query)
                query_count += 1
                    
            print(f"Success! Imported {query_count} SQL statements from 'schema.sql'.")
            
            # Seed default badges if not exist
            badges_data = [
                ("Bronze Learner", "Achieve a 7-day learning streak.", "fa-medal text-warning", "streak", 7),
                ("Silver Learner", "Achieve a 30-day learning streak.", "fa-medal text-secondary", "streak", 30),
                ("Gold Learner", "Achieve a 100-day learning streak.", "fa-medal text-warning", "streak", 100),
                ("Quiz Master", "Maintain an average quiz score of 90%.", "fa-crown text-danger", "score", 90),
                ("Course Champion", "Complete all course levels.", "fa-trophy text-primary", "completion", 1)
            ]
            
            for badge in badges_data:
                cursor.execute("SELECT id FROM badges WHERE name = %s", (badge[0],))
                if not cursor.fetchone():
                    cursor.execute(
                        "INSERT INTO badges (name, description, icon, requirement_type, requirement_value) VALUES (%s, %s, %s, %s, %s)",
                        badge
                    )
            connection.commit()
            print("Seeded default gamification badges.")
            
            print("\nDatabase configuration complete! You can now run the web app with 'python app.py'.")
            
    except Exception as e:
        print("\n❌ Error setting up database!")
        print(f"Details: {e}")
        print("\nSuggestions:")
        print("1. Make sure your MySQL Server (XAMPP/WAMP/Workbench) is running.")
        print(f"2. Double-check your user ('{Config.DB_USER}') and password in config.py.")
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

if __name__ == "__main__":
    init_database()
