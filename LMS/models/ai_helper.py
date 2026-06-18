import json
import urllib.request
import urllib.error
import os
import random
from config import Config

# =============================================================================
# COMPREHENSIVE LOCAL KNOWLEDGE BASE
# Covers: Programming, Databases, Cloud, Networking, Web Dev, OS, AI/ML,
#         Data Structures, Algorithms, Software Engineering, Cyber Security, etc.
# =============================================================================

KNOWLEDGE_BASE = {

    # ── PROGRAMMING FUNDAMENTALS ──────────────────────────────────────────
    "python": {
        "keywords": ["python", "python programming", "py"],
        "title": "🐍 Python Programming",
        "content": (
            "**Python** is a high-level, interpreted, general-purpose programming language created by **Guido van Rossum** in 1991.\n\n"
            "### Key Features\n"
            "- **Easy to learn** – clean, readable syntax that uses indentation\n"
            "- **Interpreted** – no need to compile; runs line by line\n"
            "- **Dynamically typed** – no need to declare variable types\n"
            "- **Extensive libraries** – NumPy, Pandas, Flask, Django, TensorFlow\n"
            "- **Cross-platform** – works on Windows, macOS, Linux\n\n"
            "### Data Types\n"
            "| Type | Example |\n"
            "|------|--------|\n"
            "| int | `x = 10` |\n"
            "| float | `y = 3.14` |\n"
            "| str | `name = 'Hello'` |\n"
            "| list | `items = [1, 2, 3]` |\n"
            "| dict | `data = {'key': 'value'}` |\n"
            "| tuple | `t = (1, 2)` |\n"
            "| set | `s = {1, 2, 3}` |\n"
            "| bool | `flag = True` |\n\n"
            "### Example\n"
            "```python\n"
            "# Function to check if a number is prime\n"
            "def is_prime(n):\n"
            "    if n < 2:\n"
            "        return False\n"
            "    for i in range(2, int(n**0.5) + 1):\n"
            "        if n % i == 0:\n"
            "            return False\n"
            "    return True\n\n"
            "print(is_prime(17))  # Output: True\n"
            "```\n\n"
            "### Why Python is Popular\n"
            "- Used in **Web Development** (Flask, Django)\n"
            "- Used in **Data Science & AI** (Pandas, TensorFlow)\n"
            "- Used in **Automation & Scripting**\n"
            "- Used in **Cloud Computing** (AWS Lambda, GCP Cloud Functions)\n"
        ),
    },

    "java": {
        "keywords": ["java", "java programming", "jdk", "jvm"],
        "title": "☕ Java Programming",
        "content": (
            "**Java** is a class-based, object-oriented programming language developed by **Sun Microsystems** (now Oracle) in 1995.\n\n"
            "### Key Features\n"
            "- **Platform Independent** – \"Write Once, Run Anywhere\" (WORA) via the JVM\n"
            "- **Object-Oriented** – Everything is an object (classes, inheritance, polymorphism)\n"
            "- **Strongly Typed** – Variable types must be declared\n"
            "- **Automatic Garbage Collection** – Memory management is handled automatically\n"
            "- **Multi-threaded** – Built-in support for concurrent programming\n\n"
            "### OOP Concepts in Java\n"
            "| Concept | Description |\n"
            "|---------|------------|\n"
            "| Encapsulation | Bundling data & methods together (private fields, public getters/setters) |\n"
            "| Inheritance | One class inherits properties of another (`extends`) |\n"
            "| Polymorphism | Same method behaves differently (overloading & overriding) |\n"
            "| Abstraction | Hiding implementation details (abstract classes, interfaces) |\n\n"
            "### Example\n"
            "```java\n"
            "public class HelloWorld {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Hello, World!\");\n"
            "    }\n"
            "}\n"
            "```\n"
        ),
    },

    "c_programming": {
        "keywords": ["c programming", "c language", "c program"],
        "title": "⚙️ C Programming",
        "content": (
            "**C** is a general-purpose, procedural programming language developed by **Dennis Ritchie** at Bell Labs in 1972.\n\n"
            "### Key Features\n"
            "- **Low-level access** – Direct memory manipulation via pointers\n"
            "- **Fast execution** – Compiled to machine code\n"
            "- **Portable** – Can be compiled on different platforms\n"
            "- **Foundation language** – C++, Java, Python are all influenced by C\n\n"
            "### Data Types\n"
            "| Type | Size | Example |\n"
            "|------|------|--------|\n"
            "| int | 4 bytes | `int x = 10;` |\n"
            "| float | 4 bytes | `float y = 3.14;` |\n"
            "| double | 8 bytes | `double z = 3.14159;` |\n"
            "| char | 1 byte | `char c = 'A';` |\n\n"
            "### Example\n"
            "```c\n"
            "#include <stdio.h>\n"
            "int main() {\n"
            "    int n, sum = 0;\n"
            "    printf(\"Enter a number: \");\n"
            "    scanf(\"%d\", &n);\n"
            "    for (int i = 1; i <= n; i++) {\n"
            "        sum += i;\n"
            "    }\n"
            "    printf(\"Sum = %d\\n\", sum);\n"
            "    return 0;\n"
            "}\n"
            "```\n"
        ),
    },

    "oop": {
        "keywords": ["oop", "object oriented", "oops", "encapsulation", "inheritance", "polymorphism", "abstraction"],
        "title": "🧩 Object-Oriented Programming (OOP)",
        "content": (
            "**OOP** is a programming paradigm based on the concept of **objects** which contain data (fields/attributes) and code (methods/functions).\n\n"
            "### Four Pillars of OOP\n\n"
            "#### 1. Encapsulation\n"
            "Bundling data and methods that operate on the data within a single unit (class). Access is controlled via access modifiers (`private`, `public`, `protected`).\n"
            "```python\n"
            "class BankAccount:\n"
            "    def __init__(self, balance):\n"
            "        self.__balance = balance  # Private attribute\n"
            "    def get_balance(self):\n"
            "        return self.__balance\n"
            "```\n\n"
            "#### 2. Inheritance\n"
            "A class (child) can inherit properties and methods from another class (parent), promoting code reuse.\n"
            "```python\n"
            "class Animal:\n"
            "    def speak(self):\n"
            "        return 'Some sound'\n\n"
            "class Dog(Animal):\n"
            "    def speak(self):\n"
            "        return 'Bark!'\n"
            "```\n\n"
            "#### 3. Polymorphism\n"
            "Same method name, different behavior. Achieved via **method overriding** (runtime) and **method overloading** (compile-time).\n\n"
            "#### 4. Abstraction\n"
            "Hiding complex implementation details and exposing only the necessary interface. In Python, use `ABC` (Abstract Base Class).\n\n"
            "### Types of Inheritance\n"
            "| Type | Description |\n"
            "|------|-------------|\n"
            "| Single | One parent → One child |\n"
            "| Multiple | Multiple parents → One child |\n"
            "| Multilevel | Grandparent → Parent → Child |\n"
            "| Hierarchical | One parent → Multiple children |\n"
            "| Hybrid | Combination of two or more types |\n"
        ),
    },

    # ── DATABASES ─────────────────────────────────────────────────────────
    "database": {
        "keywords": ["database", "dbms", "rdbms", "db"],
        "title": "🗄️ Database Management Systems (DBMS)",
        "content": (
            "A **Database** is an organized collection of structured data stored electronically. A **DBMS** is software that manages and controls access to the data.\n\n"
            "### Types of Databases\n"
            "| Type | Description | Examples |\n"
            "|------|-------------|----------|\n"
            "| Relational (RDBMS) | Data stored in tables with rows & columns | MySQL, PostgreSQL, Oracle |\n"
            "| NoSQL | Flexible schema for unstructured data | MongoDB, Cassandra, Redis |\n"
            "| Graph DB | Data stored as nodes & edges | Neo4j, ArangoDB |\n"
            "| Time-Series | Optimized for time-stamped data | InfluxDB, TimescaleDB |\n\n"
            "### ACID Properties (for Transactions)\n"
            "- **A**tomicity – All operations complete or none do\n"
            "- **C**onsistency – Database moves from one valid state to another\n"
            "- **I**solation – Concurrent transactions don't interfere with each other\n"
            "- **D**urability – Once committed, data survives crashes\n\n"
            "### Keys in RDBMS\n"
            "| Key Type | Purpose |\n"
            "|----------|--------|\n"
            "| Primary Key | Uniquely identifies each row |\n"
            "| Foreign Key | Links two tables together |\n"
            "| Candidate Key | Could serve as primary key |\n"
            "| Composite Key | Combination of two+ columns as key |\n"
            "| Unique Key | Ensures all values in column are unique |\n\n"
            "### Normalization\n"
            "- **1NF** – No repeating groups, atomic values\n"
            "- **2NF** – 1NF + No partial dependencies\n"
            "- **3NF** – 2NF + No transitive dependencies\n"
            "- **BCNF** – Stricter version of 3NF\n"
        ),
    },

    "sql": {
        "keywords": ["sql", "mysql", "query", "queries", "select", "insert", "update", "delete", "join"],
        "title": "📊 SQL – Structured Query Language",
        "content": (
            "**SQL** is the standard language for managing and querying relational databases.\n\n"
            "### SQL Command Categories\n"
            "| Category | Commands | Purpose |\n"
            "|----------|----------|--------|\n"
            "| DDL | CREATE, ALTER, DROP, TRUNCATE | Define database structure |\n"
            "| DML | SELECT, INSERT, UPDATE, DELETE | Manipulate data |\n"
            "| DCL | GRANT, REVOKE | Control access permissions |\n"
            "| TCL | COMMIT, ROLLBACK, SAVEPOINT | Manage transactions |\n\n"
            "### Common SQL Queries\n"
            "```sql\n"
            "-- Create a table\n"
            "CREATE TABLE students (\n"
            "    id INT PRIMARY KEY AUTO_INCREMENT,\n"
            "    name VARCHAR(100) NOT NULL,\n"
            "    email VARCHAR(100) UNIQUE,\n"
            "    department VARCHAR(50)\n"
            ");\n\n"
            "-- Insert data\n"
            "INSERT INTO students (name, email, department)\n"
            "VALUES ('Durga', 'durga@gmail.com', 'CSE');\n\n"
            "-- Select with conditions\n"
            "SELECT * FROM students WHERE department = 'CSE';\n\n"
            "-- Join two tables\n"
            "SELECT s.name, c.name AS course_name\n"
            "FROM students s\n"
            "JOIN enrollments e ON s.id = e.student_id\n"
            "JOIN courses c ON e.course_id = c.id;\n\n"
            "-- Aggregate functions\n"
            "SELECT department, COUNT(*) AS total_students\n"
            "FROM students\n"
            "GROUP BY department\n"
            "HAVING COUNT(*) > 5;\n"
            "```\n\n"
            "### Types of JOINs\n"
            "| Join | Description |\n"
            "|------|-------------|\n"
            "| INNER JOIN | Returns matching rows from both tables |\n"
            "| LEFT JOIN | All rows from left + matching from right |\n"
            "| RIGHT JOIN | All rows from right + matching from left |\n"
            "| FULL JOIN | All rows from both tables |\n"
            "| CROSS JOIN | Cartesian product of both tables |\n"
        ),
    },

    # ── CLOUD COMPUTING ───────────────────────────────────────────────────
    "cloud": {
        "keywords": ["cloud", "cloud computing", "aws", "azure", "gcp", "google cloud", "iaas", "paas", "saas"],
        "title": "☁️ Cloud Computing",
        "content": (
            "**Cloud Computing** is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing.\n\n"
            "### Service Models\n"
            "| Model | What You Manage | Example |\n"
            "|-------|----------------|--------|\n"
            "| **IaaS** (Infrastructure) | OS, Apps, Data | AWS EC2, Azure VMs |\n"
            "| **PaaS** (Platform) | Only Apps & Data | Google App Engine, Heroku |\n"
            "| **SaaS** (Software) | Nothing – just use it | Gmail, Google Docs, Salesforce |\n\n"
            "### Deployment Models\n"
            "- **Public Cloud** – Shared infrastructure (AWS, Azure, GCP)\n"
            "- **Private Cloud** – Dedicated to one organization\n"
            "- **Hybrid Cloud** – Combination of public + private\n"
            "- **Community Cloud** – Shared by organizations with common goals\n\n"
            "### Key Characteristics (NIST Definition)\n"
            "1. **On-demand self-service** – Provision resources without human interaction\n"
            "2. **Broad network access** – Available over the internet\n"
            "3. **Resource pooling** – Multi-tenant model\n"
            "4. **Rapid elasticity** – Scale up/down dynamically\n"
            "5. **Measured service** – Pay only for what you use\n\n"
            "### Top Cloud Providers\n"
            "| Provider | Key Services |\n"
            "|----------|-------------|\n"
            "| AWS | EC2, S3, Lambda, RDS, DynamoDB |\n"
            "| Azure | VMs, Blob Storage, Azure Functions |\n"
            "| GCP | Compute Engine, Cloud Storage, BigQuery |\n\n"
            "### Benefits of Cloud\n"
            "- No upfront hardware investment\n"
            "- Global scalability\n"
            "- Automatic backups & disaster recovery\n"
            "- Focus on code, not infrastructure\n"
        ),
    },

    # ── WEB DEVELOPMENT ───────────────────────────────────────────────────
    "html": {
        "keywords": ["html", "html5", "hypertext", "markup"],
        "title": "🌐 HTML – HyperText Markup Language",
        "content": (
            "**HTML** is the standard markup language used to create the **structure** of web pages.\n\n"
            "### Key HTML5 Elements\n"
            "| Element | Purpose |\n"
            "|---------|--------|\n"
            "| `<html>` | Root element of the page |\n"
            "| `<head>` | Contains meta info, title, links |\n"
            "| `<body>` | Contains visible content |\n"
            "| `<header>` | Page/section header |\n"
            "| `<nav>` | Navigation links |\n"
            "| `<main>` | Main content area |\n"
            "| `<section>` | Thematic grouping of content |\n"
            "| `<article>` | Self-contained content |\n"
            "| `<footer>` | Page/section footer |\n"
            "| `<form>` | User input form |\n"
            "| `<table>` | Tabular data |\n\n"
            "### Example\n"
            "```html\n"
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "    <meta charset=\"UTF-8\">\n"
            "    <title>My First Page</title>\n"
            "</head>\n"
            "<body>\n"
            "    <h1>Hello World!</h1>\n"
            "    <p>This is a paragraph.</p>\n"
            "    <a href=\"https://example.com\">Click here</a>\n"
            "</body>\n"
            "</html>\n"
            "```\n\n"
            "### HTML Forms\n"
            "```html\n"
            "<form action=\"/submit\" method=\"POST\">\n"
            "    <input type=\"text\" name=\"name\" placeholder=\"Your Name\">\n"
            "    <input type=\"email\" name=\"email\" placeholder=\"Email\">\n"
            "    <button type=\"submit\">Submit</button>\n"
            "</form>\n"
            "```\n"
        ),
    },

    "css": {
        "keywords": ["css", "stylesheet", "styling", "responsive", "flexbox", "grid"],
        "title": "🎨 CSS – Cascading Style Sheets",
        "content": (
            "**CSS** is used to **style and layout** HTML elements on a web page.\n\n"
            "### CSS Selectors\n"
            "| Selector | Example | Description |\n"
            "|----------|---------|-------------|\n"
            "| Element | `p { }` | Selects all `<p>` tags |\n"
            "| Class | `.card { }` | Selects elements with `class=\"card\"` |\n"
            "| ID | `#header { }` | Selects element with `id=\"header\"` |\n"
            "| Universal | `* { }` | Selects all elements |\n"
            "| Descendant | `div p { }` | Selects `<p>` inside `<div>` |\n\n"
            "### Box Model\n"
            "Every HTML element is a box with:\n"
            "- **Content** → The actual text/image\n"
            "- **Padding** → Space between content and border\n"
            "- **Border** → Surrounds the padding\n"
            "- **Margin** → Space outside the border\n\n"
            "### Flexbox (1D Layout)\n"
            "```css\n"
            ".container {\n"
            "    display: flex;\n"
            "    justify-content: center;  /* Horizontal alignment */\n"
            "    align-items: center;      /* Vertical alignment */\n"
            "    gap: 10px;\n"
            "}\n"
            "```\n\n"
            "### CSS Grid (2D Layout)\n"
            "```css\n"
            ".grid-container {\n"
            "    display: grid;\n"
            "    grid-template-columns: repeat(3, 1fr);\n"
            "    gap: 20px;\n"
            "}\n"
            "```\n\n"
            "### Responsive Design\n"
            "```css\n"
            "@media (max-width: 768px) {\n"
            "    .container {\n"
            "        flex-direction: column;\n"
            "    }\n"
            "}\n"
            "```\n"
        ),
    },

    "javascript": {
        "keywords": ["javascript", "js", "dom", "ecmascript"],
        "title": "⚡ JavaScript",
        "content": (
            "**JavaScript** is a dynamic, interpreted programming language primarily used for making web pages interactive.\n\n"
            "### Key Concepts\n"
            "| Concept | Description |\n"
            "|---------|-------------|\n"
            "| Variables | `let`, `const`, `var` |\n"
            "| Functions | `function greet() {}` or `() => {}` (arrow) |\n"
            "| DOM Manipulation | `document.getElementById()`, `querySelector()` |\n"
            "| Events | `onclick`, `addEventListener()` |\n"
            "| Promises/Async | `fetch()`, `async/await` |\n"
            "| JSON | Data interchange format |\n\n"
            "### Example – Fetch API\n"
            "```javascript\n"
            "async function getUsers() {\n"
            "    const response = await fetch('/api/users');\n"
            "    const data = await response.json();\n"
            "    console.log(data);\n"
            "}\n"
            "```\n\n"
            "### DOM Manipulation\n"
            "```javascript\n"
            "document.getElementById('btn').addEventListener('click', function() {\n"
            "    document.getElementById('output').innerText = 'Button Clicked!';\n"
            "});\n"
            "```\n"
        ),
    },

    "flask": {
        "keywords": ["flask", "flask framework", "web framework", "jinja", "jinja2"],
        "title": "🌶️ Flask Web Framework",
        "content": (
            "**Flask** is a lightweight, micro web framework for Python, created by **Armin Ronacher**.\n\n"
            "### Why Flask?\n"
            "- **Lightweight** – No forced dependencies\n"
            "- **Flexible** – Choose your own database, template engine, etc.\n"
            "- **Easy to learn** – Perfect for beginners and small-medium apps\n"
            "- **Jinja2 Templates** – Powerful HTML templating engine\n\n"
            "### Flask Project Structure\n"
            "```\n"
            "project/\n"
            "├── app.py              # Main application\n"
            "├── config.py           # Configuration\n"
            "├── templates/          # HTML templates\n"
            "│   ├── base.html\n"
            "│   └── dashboard.html\n"
            "├── static/             # CSS, JS, images\n"
            "│   ├── css/style.css\n"
            "│   └── js/script.js\n"
            "├── models/             # Database logic\n"
            "└── requirements.txt    # Dependencies\n"
            "```\n\n"
            "### Basic Flask App\n"
            "```python\n"
            "from flask import Flask, render_template, request, redirect\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route('/')\n"
            "def home():\n"
            "    return render_template('index.html')\n\n"
            "@app.route('/submit', methods=['POST'])\n"
            "def submit():\n"
            "    name = request.form.get('name')\n"
            "    return f'Hello, {name}!'\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(debug=True)\n"
            "```\n\n"
            "### Key Flask Concepts\n"
            "| Concept | Description |\n"
            "|---------|-------------|\n"
            "| Routes | URL → Function mapping (`@app.route`) |\n"
            "| Templates | HTML with Jinja2 syntax (`{{ variable }}`, `{% for %}`) |\n"
            "| Request | Access form data, query params, files |\n"
            "| Session | Store user login state |\n"
            "| Flash | Show one-time messages to user |\n"
        ),
    },

    "mvc": {
        "keywords": ["mvc", "model view controller", "design pattern", "architecture pattern"],
        "title": "🏗️ MVC Architecture Pattern",
        "content": (
            "**Model-View-Controller (MVC)** is a software design pattern that separates an application into three components:\n\n"
            "### Components\n"
            "| Component | Role | Example in Flask |\n"
            "|-----------|------|------------------|\n"
            "| **Model** | Data & business logic | `models/auth.py`, database queries |\n"
            "| **View** | User interface (what user sees) | HTML templates in `templates/` |\n"
            "| **Controller** | Handles requests & responses | Route functions in `app.py` |\n\n"
            "### How MVC Works\n"
            "```\n"
            "User Request → Controller (app.py)\n"
            "                  ↓\n"
            "           Model (database query)\n"
            "                  ↓\n"
            "           View (HTML template)\n"
            "                  ↓\n"
            "           Response → User sees the page\n"
            "```\n\n"
            "### Benefits\n"
            "- **Separation of concerns** – Each part has a single responsibility\n"
            "- **Reusability** – Models can be reused across different views\n"
            "- **Maintainability** – Easy to modify one part without breaking others\n"
            "- **Testability** – Each component can be tested independently\n\n"
            "### In This LMS Project\n"
            "- **Model**: `models/auth.py`, `models/course.py`, `models/assignment.py`\n"
            "- **View**: `templates/student/`, `templates/faculty/`, `templates/admin/`\n"
            "- **Controller**: Route functions in `app.py`\n"
        ),
    },

    # ── NETWORKING ────────────────────────────────────────────────────────
    "networking": {
        "keywords": ["network", "networking", "tcp", "ip", "osi", "protocol", "http", "https", "dns", "tcp/ip"],
        "title": "🌍 Computer Networking",
        "content": (
            "**Computer Networking** is the practice of connecting computers to share resources and communicate.\n\n"
            "### OSI Model (7 Layers)\n"
            "| Layer | Name | Protocol Examples | Function |\n"
            "|-------|------|-------------------|----------|\n"
            "| 7 | Application | HTTP, FTP, SMTP, DNS | User interaction |\n"
            "| 6 | Presentation | SSL/TLS, JPEG, ASCII | Data format/encryption |\n"
            "| 5 | Session | NetBIOS, RPC | Session management |\n"
            "| 4 | Transport | TCP, UDP | Reliable delivery |\n"
            "| 3 | Network | IP, ICMP, ARP | Routing & addressing |\n"
            "| 2 | Data Link | Ethernet, Wi-Fi, MAC | Frame delivery |\n"
            "| 1 | Physical | Cables, Hubs, Signals | Bit transmission |\n\n"
            "### TCP vs UDP\n"
            "| Feature | TCP | UDP |\n"
            "|---------|-----|-----|\n"
            "| Connection | Connection-oriented | Connectionless |\n"
            "| Reliability | Reliable (acknowledgments) | Unreliable (no guarantees) |\n"
            "| Speed | Slower | Faster |\n"
            "| Use Case | Web, Email, File Transfer | Streaming, Gaming, DNS |\n\n"
            "### Key Protocols\n"
            "- **HTTP/HTTPS** – Web page delivery (port 80/443)\n"
            "- **DNS** – Domain name → IP address resolution\n"
            "- **DHCP** – Automatic IP address assignment\n"
            "- **FTP** – File transfer (port 21)\n"
            "- **SSH** – Secure remote access (port 22)\n"
            "- **SMTP** – Email sending (port 25)\n"
        ),
    },

    # ── OPERATING SYSTEMS ─────────────────────────────────────────────────
    "os": {
        "keywords": ["operating system", "os", "process", "thread", "scheduling", "memory management", "deadlock"],
        "title": "💻 Operating Systems",
        "content": (
            "An **Operating System (OS)** is system software that manages computer hardware and provides services for application programs.\n\n"
            "### Functions of an OS\n"
            "- **Process Management** – Creating, scheduling, terminating processes\n"
            "- **Memory Management** – Allocating/deallocating RAM\n"
            "- **File System Management** – Organizing files and directories\n"
            "- **I/O Management** – Managing input/output devices\n"
            "- **Security** – User authentication and access control\n\n"
            "### Process vs Thread\n"
            "| Feature | Process | Thread |\n"
            "|---------|---------|--------|\n"
            "| Memory | Separate memory space | Shares parent's memory |\n"
            "| Overhead | Heavy | Lightweight |\n"
            "| Communication | IPC (pipes, sockets) | Shared variables |\n"
            "| Crash Impact | Other processes unaffected | May crash entire process |\n\n"
            "### CPU Scheduling Algorithms\n"
            "| Algorithm | Description |\n"
            "|-----------|-------------|\n"
            "| FCFS | First Come, First Served |\n"
            "| SJF | Shortest Job First |\n"
            "| Round Robin | Fixed time quantum for each process |\n"
            "| Priority | Based on priority number |\n"
            "| Multilevel Queue | Multiple queues with different algorithms |\n\n"
            "### Deadlock Conditions (All 4 must hold)\n"
            "1. **Mutual Exclusion** – Only one process can use a resource at a time\n"
            "2. **Hold and Wait** – Process holds one resource and waits for another\n"
            "3. **No Preemption** – Resources cannot be forcibly taken\n"
            "4. **Circular Wait** – A circular chain of processes waiting for each other\n"
        ),
    },

    # ── DATA STRUCTURES ───────────────────────────────────────────────────
    "data_structures": {
        "keywords": ["data structure", "array", "linked list", "stack", "queue", "tree", "graph", "hash", "heap"],
        "title": "📦 Data Structures",
        "content": (
            "**Data Structures** are ways of organizing and storing data for efficient access and modification.\n\n"
            "### Common Data Structures\n"
            "| Structure | Description | Time (Access) | Time (Search) |\n"
            "|-----------|-------------|---------------|----------------|\n"
            "| Array | Contiguous memory block | O(1) | O(n) |\n"
            "| Linked List | Nodes connected by pointers | O(n) | O(n) |\n"
            "| Stack | LIFO (Last In, First Out) | O(n) | O(n) |\n"
            "| Queue | FIFO (First In, First Out) | O(n) | O(n) |\n"
            "| Hash Table | Key-value pairs | O(1) avg | O(1) avg |\n"
            "| Binary Tree | Hierarchical with max 2 children | O(log n) | O(log n) |\n"
            "| Heap | Complete binary tree (min/max) | O(1) top | O(n) |\n"
            "| Graph | Nodes + Edges | – | O(V+E) BFS/DFS |\n\n"
            "### Stack vs Queue\n"
            "| Feature | Stack | Queue |\n"
            "|---------|-------|-------|\n"
            "| Principle | LIFO | FIFO |\n"
            "| Insert | push() (top) | enqueue() (rear) |\n"
            "| Remove | pop() (top) | dequeue() (front) |\n"
            "| Example | Undo/Redo, Recursion | Print queue, BFS |\n\n"
            "### Python Examples\n"
            "```python\n"
            "# Stack using list\n"
            "stack = []\n"
            "stack.append(10)   # push\n"
            "stack.append(20)\n"
            "stack.pop()        # returns 20 (LIFO)\n\n"
            "# Queue using deque\n"
            "from collections import deque\n"
            "queue = deque()\n"
            "queue.append(10)   # enqueue\n"
            "queue.append(20)\n"
            "queue.popleft()    # returns 10 (FIFO)\n"
            "```\n"
        ),
    },

    # ── ALGORITHMS ────────────────────────────────────────────────────────
    "algorithms": {
        "keywords": ["algorithm", "sorting", "searching", "binary search", "bubble sort", "merge sort", "quick sort", "time complexity", "big o"],
        "title": "⚡ Algorithms & Complexity",
        "content": (
            "An **Algorithm** is a step-by-step procedure for solving a problem or performing a computation.\n\n"
            "### Big O Notation (Time Complexity)\n"
            "| Notation | Name | Example |\n"
            "|----------|------|--------|\n"
            "| O(1) | Constant | Array access by index |\n"
            "| O(log n) | Logarithmic | Binary search |\n"
            "| O(n) | Linear | Linear search |\n"
            "| O(n log n) | Linearithmic | Merge sort, Quick sort (avg) |\n"
            "| O(n²) | Quadratic | Bubble sort, Selection sort |\n"
            "| O(2ⁿ) | Exponential | Recursive Fibonacci |\n\n"
            "### Sorting Algorithms\n"
            "| Algorithm | Best | Average | Worst | Stable? |\n"
            "|-----------|------|---------|-------|---------|\n"
            "| Bubble Sort | O(n) | O(n²) | O(n²) | Yes |\n"
            "| Selection Sort | O(n²) | O(n²) | O(n²) | No |\n"
            "| Insertion Sort | O(n) | O(n²) | O(n²) | Yes |\n"
            "| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Yes |\n"
            "| Quick Sort | O(n log n) | O(n log n) | O(n²) | No |\n\n"
            "### Binary Search (Python)\n"
            "```python\n"
            "def binary_search(arr, target):\n"
            "    low, high = 0, len(arr) - 1\n"
            "    while low <= high:\n"
            "        mid = (low + high) // 2\n"
            "        if arr[mid] == target:\n"
            "            return mid\n"
            "        elif arr[mid] < target:\n"
            "            low = mid + 1\n"
            "        else:\n"
            "            high = mid - 1\n"
            "    return -1\n"
            "```\n"
        ),
    },

    # ── AI & MACHINE LEARNING ─────────────────────────────────────────────
    "ai_ml": {
        "keywords": ["artificial intelligence", "ai", "machine learning", "ml", "deep learning", "neural network", "supervised", "unsupervised"],
        "title": "🤖 Artificial Intelligence & Machine Learning",
        "content": (
            "**Artificial Intelligence (AI)** is the simulation of human intelligence in machines. **Machine Learning (ML)** is a subset of AI that learns from data.\n\n"
            "### AI vs ML vs DL\n"
            "| Concept | Scope |\n"
            "|---------|-------|\n"
            "| **AI** | Broadest – any smart behavior by machines |\n"
            "| **ML** | Subset of AI – learning from data |\n"
            "| **Deep Learning** | Subset of ML – neural networks with many layers |\n\n"
            "### Types of Machine Learning\n"
            "| Type | Description | Examples |\n"
            "|------|-------------|----------|\n"
            "| **Supervised** | Labeled data (input→output) | Spam detection, Image classification |\n"
            "| **Unsupervised** | No labels, find patterns | Clustering, Recommendation |\n"
            "| **Reinforcement** | Learn by rewards/penalties | Game AI, Self-driving cars |\n\n"
            "### Common ML Algorithms\n"
            "- **Linear Regression** – Predicting continuous values\n"
            "- **Logistic Regression** – Binary classification\n"
            "- **Decision Tree** – Tree-based classification/regression\n"
            "- **Random Forest** – Ensemble of decision trees\n"
            "- **K-Nearest Neighbors (KNN)** – Classification by proximity\n"
            "- **Support Vector Machine (SVM)** – Finding optimal decision boundary\n"
            "- **Neural Networks** – Layers of interconnected nodes (neurons)\n\n"
            "### Neural Network Basics\n"
            "```\n"
            "Input Layer → Hidden Layers → Output Layer\n"
            "   (x)     →   (weights, biases, activation)   →   (ŷ)\n"
            "```\n"
            "- **Activation Functions**: ReLU, Sigmoid, Softmax, Tanh\n"
            "- **Loss Functions**: MSE (regression), Cross-Entropy (classification)\n"
            "- **Optimizer**: SGD, Adam\n"
        ),
    },

    # ── CYBER SECURITY ────────────────────────────────────────────────────
    "security": {
        "keywords": ["security", "cyber security", "encryption", "hacking", "firewall", "authentication", "authorization"],
        "title": "🔒 Cyber Security",
        "content": (
            "**Cyber Security** is the practice of protecting systems, networks, and programs from digital attacks.\n\n"
            "### CIA Triad\n"
            "| Principle | Description |\n"
            "|-----------|-------------|\n"
            "| **Confidentiality** | Data is accessible only to authorized users |\n"
            "| **Integrity** | Data is accurate and unaltered |\n"
            "| **Availability** | Systems are operational when needed |\n\n"
            "### Common Attack Types\n"
            "| Attack | Description |\n"
            "|--------|-------------|\n"
            "| SQL Injection | Malicious SQL queries via input fields |\n"
            "| XSS | Injecting malicious scripts into web pages |\n"
            "| CSRF | Tricking users into performing unintended actions |\n"
            "| DDoS | Overwhelming a server with traffic |\n"
            "| Phishing | Fake emails/websites to steal credentials |\n"
            "| Man-in-the-Middle | Intercepting communication between two parties |\n\n"
            "### Encryption\n"
            "- **Symmetric**: Same key to encrypt & decrypt (AES, DES)\n"
            "- **Asymmetric**: Public key encrypts, Private key decrypts (RSA, ECC)\n"
            "- **Hashing**: One-way function, no decryption (SHA-256, bcrypt, MD5)\n\n"
            "### Authentication vs Authorization\n"
            "| Concept | Description |\n"
            "|---------|-------------|\n"
            "| Authentication | Verifying identity (\"Who are you?\") → Login |\n"
            "| Authorization | Verifying access rights (\"What can you do?\") → Permissions |\n"
        ),
    },

    # ── SOFTWARE ENGINEERING ──────────────────────────────────────────────
    "sdlc": {
        "keywords": ["sdlc", "software engineering", "agile", "waterfall", "scrum", "software development"],
        "title": "🔧 Software Development Life Cycle (SDLC)",
        "content": (
            "**SDLC** is the structured process of planning, creating, testing, and deploying a software application.\n\n"
            "### SDLC Phases\n"
            "1. **Planning** – Define project scope, feasibility study\n"
            "2. **Requirements Analysis** – Gather and document user requirements\n"
            "3. **Design** – System architecture, database design, UI mockups\n"
            "4. **Implementation (Coding)** – Actual development\n"
            "5. **Testing** – Unit, Integration, System, Acceptance testing\n"
            "6. **Deployment** – Release to production\n"
            "7. **Maintenance** – Bug fixes, updates, enhancements\n\n"
            "### SDLC Models\n"
            "| Model | Description | Best For |\n"
            "|-------|-------------|----------|\n"
            "| **Waterfall** | Sequential, each phase completed before next | Small, well-defined projects |\n"
            "| **Agile** | Iterative, continuous feedback | Most modern projects |\n"
            "| **Scrum** | Agile framework with sprints | Team-based development |\n"
            "| **Spiral** | Iterative with risk analysis | Large, high-risk projects |\n"
            "| **V-Model** | Verification & Validation in parallel | Safety-critical systems |\n"
            "| **DevOps** | Continuous integration & deployment | Cloud-native apps |\n\n"
            "### Agile Principles\n"
            "- Deliver working software frequently\n"
            "- Welcome changing requirements\n"
            "- Close collaboration between business & developers\n"
            "- Face-to-face communication is preferred\n"
        ),
    },

    # ── API ───────────────────────────────────────────────────────────────
    "api": {
        "keywords": ["api", "rest", "restful", "endpoint", "get", "post", "put", "patch"],
        "title": "🔌 APIs – Application Programming Interfaces",
        "content": (
            "An **API** is a set of rules that allows two software applications to communicate with each other.\n\n"
            "### REST API Methods\n"
            "| Method | Purpose | Example |\n"
            "|--------|---------|--------|\n"
            "| GET | Retrieve data | `GET /api/students` |\n"
            "| POST | Create new data | `POST /api/students` |\n"
            "| PUT | Update entire resource | `PUT /api/students/1` |\n"
            "| PATCH | Partial update | `PATCH /api/students/1` |\n"
            "| DELETE | Remove data | `DELETE /api/students/1` |\n\n"
            "### HTTP Status Codes\n"
            "| Code | Meaning |\n"
            "|------|--------|\n"
            "| 200 | OK – Success |\n"
            "| 201 | Created – Resource created |\n"
            "| 400 | Bad Request – Invalid input |\n"
            "| 401 | Unauthorized – Not logged in |\n"
            "| 403 | Forbidden – No permission |\n"
            "| 404 | Not Found – Resource doesn't exist |\n"
            "| 500 | Internal Server Error |\n\n"
            "### Flask API Example\n"
            "```python\n"
            "from flask import Flask, jsonify, request\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route('/api/students', methods=['GET'])\n"
            "def get_students():\n"
            "    students = [{'id': 1, 'name': 'Durga'}]\n"
            "    return jsonify(students), 200\n\n"
            "@app.route('/api/students', methods=['POST'])\n"
            "def create_student():\n"
            "    data = request.get_json()\n"
            "    return jsonify({'message': 'Student created!'}), 201\n"
            "```\n"
        ),
    },

    # ── GIT VERSION CONTROL ───────────────────────────────────────────────
    "git": {
        "keywords": ["git", "github", "version control", "commit", "branch", "merge", "pull request"],
        "title": "🔀 Git & Version Control",
        "content": (
            "**Git** is a distributed version control system for tracking code changes. **GitHub** is a cloud platform to host Git repositories.\n\n"
            "### Essential Git Commands\n"
            "```bash\n"
            "# Initialize a new repository\n"
            "git init\n\n"
            "# Stage changes\n"
            "git add .                    # Stage all files\n"
            "git add filename.py         # Stage specific file\n\n"
            "# Commit changes\n"
            "git commit -m \"Added login feature\"\n\n"
            "# Check status & history\n"
            "git status\n"
            "git log --oneline\n\n"
            "# Branching\n"
            "git branch feature-login    # Create branch\n"
            "git checkout feature-login  # Switch to branch\n"
            "git merge feature-login     # Merge into current branch\n\n"
            "# Remote (GitHub)\n"
            "git remote add origin https://github.com/user/repo.git\n"
            "git push -u origin main\n"
            "git pull origin main\n"
            "```\n\n"
            "### Git Workflow\n"
            "```\n"
            "Working Directory → Staging Area → Local Repo → Remote Repo\n"
            "   (git add)        (git commit)     (git push)\n"
            "```\n"
        ),
    },

    # ── BOOTSTRAP ─────────────────────────────────────────────────────────
    "bootstrap": {
        "keywords": ["bootstrap", "bootstrap 5", "responsive design", "grid system"],
        "title": "🅱️ Bootstrap Framework",
        "content": (
            "**Bootstrap** is a popular CSS framework for building responsive, mobile-first websites quickly.\n\n"
            "### Grid System (12-column)\n"
            "```html\n"
            "<div class=\"container\">\n"
            "    <div class=\"row\">\n"
            "        <div class=\"col-md-6\">Left Half</div>\n"
            "        <div class=\"col-md-6\">Right Half</div>\n"
            "    </div>\n"
            "</div>\n"
            "```\n\n"
            "### Breakpoints\n"
            "| Prefix | Screen Size |\n"
            "|--------|------------|\n"
            "| `col-` | Extra small (<576px) |\n"
            "| `col-sm-` | Small (≥576px) |\n"
            "| `col-md-` | Medium (≥768px) |\n"
            "| `col-lg-` | Large (≥992px) |\n"
            "| `col-xl-` | Extra large (≥1200px) |\n\n"
            "### Useful Components\n"
            "- **Navbar** – Responsive navigation bar\n"
            "- **Cards** – Flexible content containers\n"
            "- **Modals** – Popup dialog boxes\n"
            "- **Forms** – Styled input fields & buttons\n"
            "- **Alerts** – Notification messages\n"
            "- **Badges** – Small count/label indicators\n"
        ),
    },

    # ── LMS PROJECT SPECIFIC ──────────────────────────────────────────────
    "lms_project": {
        "keywords": ["lms", "learning management", "this project", "our project", "cloud lms"],
        "title": "📚 About This Cloud LMS Project",
        "content": (
            "This **AI-Powered Cloud Learning Management System** is built using:\n\n"
            "### Tech Stack\n"
            "| Component | Technology |\n"
            "|-----------|------------|\n"
            "| Backend | Python Flask |\n"
            "| Frontend | HTML5, CSS3, Bootstrap 5 |\n"
            "| Database | MySQL (PyMySQL connector) |\n"
            "| Architecture | MVC (Model-View-Controller) |\n"
            "| AI Feature | Rule-based chatbot + Gemini API support |\n\n"
            "### Features\n"
            "- **Student Module**: Register, enroll in courses, download materials, submit assignments, view marks\n"
            "- **Faculty Module**: Create courses, upload notes, create assignments, grade submissions\n"
            "- **Admin Module**: Manage all users, courses, and system statistics\n"
            "- **AI Study Assistant**: Get quizzes, summaries, and explanations\n"
            "- **Notifications**: System-wide notifications for all user roles\n\n"
            "### Database Tables\n"
            "- `admins`, `faculty`, `students` – User tables\n"
            "- `courses`, `enrollments` – Course management\n"
            "- `course_materials` – Study materials (PDFs, docs)\n"
            "- `assignments`, `submissions` – Assignment workflow\n"
            "- `marks` – Grading & feedback\n"
            "- `notifications` – System notifications\n"
        ),
    },
}

# =============================================================================
# QUIZ BANK – Organized by Subject
# =============================================================================

QUIZ_BANK = {
    "python": [
        {"q": "What is the output of `print(type([]))` in Python?", "a": "`<class 'list'>` – Square brackets create a list.", "options": ["A) `<class 'tuple'>`", "B) `<class 'list'>` ✅", "C) `<class 'dict'>`", "D) `<class 'array'>`"]},
        {"q": "Which keyword is used to define a function in Python?", "a": "`def` is used to define functions.", "options": ["A) function", "B) fun", "C) def ✅", "D) define"]},
        {"q": "What does `len('Hello')` return?", "a": "`5` – It counts the number of characters.", "options": ["A) 4", "B) 5 ✅", "C) 6", "D) Error"]},
        {"q": "Which of the following is immutable in Python?", "a": "Tuples are immutable (cannot be changed after creation).", "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple ✅"]},
        {"q": "What does `//` operator do in Python?", "a": "Floor division – divides and rounds down to the nearest integer.", "options": ["A) Modulus", "B) Exponentiation", "C) Floor Division ✅", "D) True Division"]},
    ],
    "database": [
        {"q": "Which SQL clause is used to filter rows?", "a": "`WHERE` clause filters rows based on conditions.", "options": ["A) GROUP BY", "B) ORDER BY", "C) WHERE ✅", "D) HAVING"]},
        {"q": "What does the PRIMARY KEY constraint ensure?", "a": "Uniquely identifies each record in a table.", "options": ["A) Values can be NULL", "B) Values must be unique and NOT NULL ✅", "C) Values are auto-sorted", "D) Values are encrypted"]},
        {"q": "Which normal form removes transitive dependencies?", "a": "Third Normal Form (3NF) eliminates transitive dependencies.", "options": ["A) 1NF", "B) 2NF", "C) 3NF ✅", "D) BCNF"]},
        {"q": "What does a FOREIGN KEY do?", "a": "It creates a link between two tables by referencing the PRIMARY KEY of another table.", "options": ["A) Makes a column unique", "B) Links two tables together ✅", "C) Encrypts data", "D) Creates an index"]},
        {"q": "Which SQL command is used to remove all rows from a table without deleting the table?", "a": "`TRUNCATE` removes all rows but keeps the table structure.", "options": ["A) DELETE", "B) DROP", "C) TRUNCATE ✅", "D) REMOVE"]},
    ],
    "cloud": [
        {"q": "What does SaaS stand for?", "a": "Software as a Service – e.g., Gmail, Google Docs.", "options": ["A) System as a Service", "B) Software as a Service ✅", "C) Storage as a Service", "D) Security as a Service"]},
        {"q": "Which is NOT a cloud deployment model?", "a": "Desktop Cloud is not a recognized model.", "options": ["A) Public Cloud", "B) Private Cloud", "C) Hybrid Cloud", "D) Desktop Cloud ✅"]},
        {"q": "AWS EC2 is an example of which service model?", "a": "IaaS – You manage the OS and applications on virtual machines.", "options": ["A) SaaS", "B) PaaS", "C) IaaS ✅", "D) FaaS"]},
        {"q": "What is the key benefit of cloud elasticity?", "a": "Ability to scale resources up or down based on demand.", "options": ["A) Free unlimited storage", "B) Automatic scaling based on demand ✅", "C) No internet required", "D) Faster CPU speeds"]},
    ],
    "networking": [
        {"q": "How many layers does the OSI model have?", "a": "7 layers – Physical, Data Link, Network, Transport, Session, Presentation, Application.", "options": ["A) 4", "B) 5", "C) 6", "D) 7 ✅"]},
        {"q": "Which protocol is used for secure web browsing?", "a": "HTTPS (HTTP + TLS/SSL encryption) on port 443.", "options": ["A) HTTP", "B) FTP", "C) HTTPS ✅", "D) SMTP"]},
        {"q": "What does DNS stand for?", "a": "Domain Name System – translates domain names to IP addresses.", "options": ["A) Data Network System", "B) Domain Name System ✅", "C) Digital Name Server", "D) Dynamic Network Service"]},
    ],
    "general": [
        {"q": "What does CPU stand for?", "a": "Central Processing Unit – the 'brain' of the computer.", "options": ["A) Central Processing Unit ✅", "B) Computer Personal Unit", "C) Central Program Utility", "D) Computer Processing Utility"]},
        {"q": "Which data structure uses LIFO (Last In, First Out)?", "a": "Stack – the last element added is the first one removed.", "options": ["A) Queue", "B) Stack ✅", "C) Array", "D) Linked List"]},
        {"q": "What is the time complexity of binary search?", "a": "O(log n) – it halves the search space each step.", "options": ["A) O(n)", "B) O(n²)", "C) O(log n) ✅", "D) O(1)"]},
        {"q": "In MVC, what does 'M' stand for?", "a": "Model – represents data and business logic.", "options": ["A) Main", "B) Model ✅", "C) Module", "D) Manager"]},
        {"q": "What does HTML stand for?", "a": "HyperText Markup Language – used to structure web pages.", "options": ["A) Hyper Transfer Markup Language", "B) HyperText Markup Language ✅", "C) High-Level Text Management Language", "D) HyperText Machine Language"]},
    ],
}

# =============================================================================
# STUDY TIPS – More comprehensive
# =============================================================================

STUDY_TIPS = [
    "📅 **Create a Study Schedule** – Allocate specific time slots for each subject. Consistency beats cramming!",
    "✍️ **Write Code Daily** – Programming is learned by doing, not just reading. Write at least 10 lines of code every day.",
    "🧠 **Use Active Recall** – After reading a topic, close the book and try to explain it in your own words.",
    "📝 **Make Short Notes** – Summarize each chapter in your own handwriting. This improves memory retention by 40%.",
    "🔁 **Spaced Repetition** – Review topics after 1 day, 3 days, 7 days, and 14 days to move them to long-term memory.",
    "💻 **Build Mini Projects** – Apply what you learn by building small projects (calculator, to-do app, portfolio site).",
    "👥 **Teach Someone Else** – If you can explain a concept to a friend, you truly understand it (Feynman Technique).",
    "🎯 **Focus on Understanding, Not Memorizing** – Understand the 'WHY' behind each concept, not just the 'WHAT'.",
    "⏰ **Start Assignments Early** – Debugging always takes longer than expected, especially with databases and servers.",
    "📊 **Practice with Mock Tests** – Use the quiz feature here to test yourself before exams!",
]

# =============================================================================
# GREETING RESPONSES
# =============================================================================

GREETINGS = {
    "keywords": ["hello", "hi", "hey", "good morning", "good evening", "good afternoon", "howdy", "hai", "vanakkam", "namaste"],
    "responses": [
        "Hello! 👋 I'm your AI Study Assistant. How can I help you today?\n\nYou can ask me about:\n- 📚 Any CS topic (Python, SQL, Cloud, Networking, etc.)\n- 📝 Practice quizzes\n- 💡 Study tips\n- 🏗️ This LMS project",
        "Hey there! 😊 Ready to learn something new? Ask me about any programming or CS concept!",
        "Hi! 🤖 I'm here to help you study. Try asking me questions like:\n- \"Explain database normalization\"\n- \"Give me a Python quiz\"\n- \"What is cloud computing?\"\n- \"Study tips for exams\"",
    ]
}

# =============================================================================
# MAIN FUNCTION
# =============================================================================

def ask_ai_assistant(user_prompt, course_details=None):
    """
    Asks the AI assistant for help.
    If 'api_key.txt' exists or GEMINI_API_KEY is available in os.environ, it queries Google Gemini API.
    Otherwise, it runs the comprehensive local pattern-matching responder.
    """
    api_key = os.environ.get('GEMINI_API_KEY', '').strip()
    
    # Try to read from api_key.txt if env variable is not set
    if not api_key:
        key_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api_key.txt')
        if os.path.exists(key_path):
            with open(key_path, 'r') as f:
                api_key = f.read().strip()
    
    # Context building
    course_context = ""
    if course_details:
        course_context = f"Context: The student is studying the course '{course_details.get('name', '')}' (Code: {course_details.get('code', '')}). Course Description: {course_details.get('description', '')}.\n"

    if api_key:
        try:
            return query_gemini_api(api_key, user_prompt, course_context)
        except Exception as e:
            print(f"Gemini API Error: {e}. Falling back to Local AI responder...")
            return generate_local_response(user_prompt, course_details)
    else:
        return generate_local_response(user_prompt, course_details)


def query_gemini_api(api_key, prompt, context=""):
    """
    Queries Google's Gemini API using standard python library urllib.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    system_instruction = (
        "You are an AI Study Assistant inside a Cloud Learning Management System (LMS). "
        "Your goal is to explain academic and programming concepts to students in a clear, friendly, and structured manner. "
        "Use markdown formatting, bullet points, code examples, and tables to make your answers easy to digest. "
        "If asked for quizzes, generate multiple-choice questions with answers. "
        "If asked about study tips, give practical, actionable advice. "
        "Always be encouraging and supportive."
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{system_instruction}\n\n{context}\nStudent Question: {prompt}"}
                ]
            }
        ]
    }
    
    headers = {"Content-Type": "application/json"}
    req_data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(url, data=req_data, headers=headers, method="POST")
    
    with urllib.request.urlopen(req, timeout=15) as response:
        res_data = response.read().decode("utf-8")
        res_json = json.loads(res_data)
        
        candidates = res_json.get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "No response text found.")
        
        return "I received your request, but could not parse the response. Try again."


def generate_local_response(prompt, course_details=None):
    """
    Comprehensive offline/local rule-based AI responder.
    Matches user queries against a rich knowledge base using keyword scoring.
    """
    p = prompt.lower().strip()
    course_name = course_details.get('name', 'General Studies') if course_details else 'General Studies'
    course_code = course_details.get('code', '') if course_details else ''

    # ── Check for greetings ──
    if any(greet in p for greet in GREETINGS["keywords"]):
        if len(p.split()) <= 4:  # Short greeting message
            return f"### 🤖 AI Study Assistant\n\n{random.choice(GREETINGS['responses'])}"

    # ── Check for quiz/test requests ──
    if any(word in p for word in ['quiz', 'test', 'question', 'exam', 'practice', 'mcq', 'mock']):
        return generate_quiz(p, course_name, course_code)

    # ── Check for study tips ──
    if any(word in p for word in ['tips', 'study tips', 'how to study', 'prepare', 'strategy', 'study guide', 'exam preparation']):
        return generate_study_tips(course_name)

    # ── Check for summary requests ──
    if any(word in p for word in ['summary', 'summarize', 'overview', 'outline', 'syllabus']):
        return generate_summary(course_name, course_details)

    # ── Check for "what is" / "explain" / "define" / "tell me about" questions ──
    is_question = any(p.startswith(q) for q in ['what is', 'what are', 'explain', 'define', 'tell me about', 'describe', 'how does', 'how do', 'what does', 'difference between', 'compare'])

    # ── Score-based topic matching ──
    best_topic = None
    best_score = 0

    for topic_key, topic_data in KNOWLEDGE_BASE.items():
        score = 0
        for keyword in topic_data["keywords"]:
            if keyword in p:
                # Longer keyword matches are more specific, so score higher
                score += len(keyword.split())
        if score > best_score:
            best_score = score
            best_topic = topic_data

    if best_topic and best_score > 0:
        response = f"### {best_topic['title']}\n\n{best_topic['content']}"
        # Add follow-up suggestions
        response += "\n\n---\n💬 **Follow-up suggestions:**\n"
        response += f"- Type **`quiz`** to get practice questions on this topic\n"
        response += f"- Type **`study tips`** for exam preparation strategies\n"
        response += f"- Ask about another topic: *database, cloud, python, networking, etc.*\n"
        return response

    # ── Check for "thank" / positive feedback ──
    if any(word in p for word in ['thank', 'thanks', 'awesome', 'great', 'good', 'nice', 'helpful', 'perfect']):
        return (
            "### 😊 You're welcome!\n\n"
            "I'm glad I could help! Feel free to ask me anything else.\n\n"
            "Here are some things you can try:\n"
            "- 📝 **`quiz`** – Take a practice test\n"
            "- 📚 **`explain [topic]`** – Learn about any CS concept\n"
            "- 💡 **`study tips`** – Get exam preparation strategies\n"
            "- 🏗️ **`explain this project`** – Learn about this LMS\n"
        )

    # ── Check for "who are you" / "what can you do" ──
    if any(phrase in p for phrase in ['who are you', 'what can you do', 'help me', 'what are you', 'your features']):
        return (
            "### 🤖 I'm Your AI Study Assistant!\n\n"
            "I'm built into this Cloud LMS to help you learn and prepare for exams. Here's what I can do:\n\n"
            "| Command | What I Do |\n"
            "|---------|----------|\n"
            "| `explain [topic]` | Detailed explanation of any CS topic |\n"
            "| `quiz` | Practice MCQ questions |\n"
            "| `study tips` | Exam preparation strategies |\n"
            "| `summarize` | Get a summary of the current course |\n"
            "| `ask anything` | I will read your course description and answer exactly based on it! |\n\n"
            "Just type your question naturally! 🎓\n"
        )

    # ── DYNAMIC COURSE QA (Exact Answer extraction) ──
    if course_details and course_details.get('description'):
        desc = course_details.get('description', '')
        # Split description into sentences
        import re
        sentences = [s.strip() for s in re.split(r'[.!?\n]', desc) if s.strip()]
        
        # Remove common stop words from prompt for better matching
        stop_words = {'what', 'is', 'the', 'a', 'an', 'how', 'do', 'i', 'tell', 'me', 'about', 'explain', 'in', 'of', 'for', 'to', 'and', 'are'}
        prompt_words = [w for w in p.split() if w not in stop_words and len(w) > 2]
        
        if prompt_words:
            best_sentence = ""
            max_matches = 0
            
            for sentence in sentences:
                sentence_words = set(sentence.lower().split())
                matches = sum(1 for w in prompt_words if w in sentence_words or any(w in sw or sw in w for sw in sentence_words))
                if matches > max_matches:
                    max_matches = matches
                    best_sentence = sentence
                    
            if max_matches > 0:
                return (
                    f"### 💡 Based on your Course ({course_name}):\n\n"
                    f"> **{best_sentence}.**\n\n"
                    f"*(I extracted this exact answer directly from your course contents!)*\n"
                )

    # ── Default: No match found ──
    return (
        f"### 🤖 AI Study Assistant\n\n"
        f"I didn't find a specific match for: **\"{prompt}\"** in my general knowledge base or your course description.\n\n"
        f"Try asking questions specifically about the topics mentioned in the **{course_name}** syllabus!\n"
    )


def generate_quiz(prompt, course_name, course_code):
    """Generate a quiz based on the detected topic."""
    p = prompt.lower()
    
    # Detect which quiz topic
    quiz_topic = "general"
    if any(w in p for w in ["python", "py"]):
        quiz_topic = "python"
    elif any(w in p for w in ["database", "sql", "dbms", "mysql"]):
        quiz_topic = "database"
    elif any(w in p for w in ["cloud", "aws", "azure"]):
        quiz_topic = "cloud"
    elif any(w in p for w in ["network", "osi", "tcp", "protocol"]):
        quiz_topic = "networking"

    questions = QUIZ_BANK.get(quiz_topic, QUIZ_BANK["general"])
    
    # Randomly select up to 5 questions
    selected = random.sample(questions, min(5, len(questions)))
    
    topic_display = quiz_topic.replace("_", " ").title()
    response = f"### 📝 Practice Quiz: **{topic_display}**\n"
    response += f"*Course: {course_name} ({course_code})*\n\n"
    response += "---\n\n"
    
    for i, q in enumerate(selected, 1):
        response += f"**Question {i}:** {q['q']}\n\n"
        for opt in q['options']:
            response += f"   {opt}\n\n"
        response += f"📖 *Explanation: {q['a']}*\n\n"
        if i < len(selected):
            response += "---\n\n"
    
    response += "\n\n✅ **Score yourself!** How many did you get right?\n"
    response += "💬 Type **`quiz`** again for a new set of questions, or ask me to **`explain`** any topic!\n"
    return response


def generate_study_tips(course_name):
    """Generate study tips."""
    selected_tips = random.sample(STUDY_TIPS, min(6, len(STUDY_TIPS)))
    
    response = f"### 💡 Study Tips for **{course_name}**\n\n"
    response += "Here are proven strategies to ace your exams:\n\n"
    for tip in selected_tips:
        response += f"- {tip}\n"
    
    response += "\n\n---\n"
    response += "🎯 **Quick Action Plan:**\n"
    response += "1. Pick one topic from your course today\n"
    response += "2. Study it for 25 minutes (Pomodoro Technique)\n"
    response += "3. Take a 5-minute break\n"
    response += "4. Test yourself with a quiz: type **`quiz`**\n"
    response += "5. Repeat with the next topic!\n"
    return response


def generate_summary(course_name, course_details=None):
    """Generate a course summary."""
    response = f"### 📖 Course Summary: **{course_name}**\n\n"
    
    if course_details and course_details.get('description'):
        desc = course_details.get('description')
        response += f"**Course Description:** {desc}\n\n"
    
    response += "**Core Learning Areas:**\n\n"
    response += "| Area | Description |\n"
    response += "|------|-------------|\n"
    response += "| 📘 Foundational Theory | Core definitions, principles, and historical context |\n"
    response += "| 💻 Practical Implementation | Hands-on coding, projects, and real-world applications |\n"
    response += "| 📊 Analysis & Design | Problem-solving, system design, and critical evaluation |\n"
    response += "| 🔬 Research & Innovation | Emerging trends and cutting-edge technologies |\n\n"
    response += "**Study Approach:**\n"
    response += "1. Start with foundational concepts (definitions, terminology)\n"
    response += "2. Move to practical exercises (code examples, labs)\n"
    response += "3. Work on assignments and mini-projects\n"
    response += "4. Review and revise using quizzes\n\n"
    response += "---\n"
    response += "💬 Type **`quiz`** to test your knowledge or **`study tips`** for exam strategies!\n"
    return response

def generate_level_quiz_json(course_context):
    """
    Generates a 5-question MCQ JSON array based on course context.
    If Gemini API is available, uses it. Otherwise, returns a fallback generic quiz.
    """
    api_key = os.environ.get('GEMINI_API_KEY', '').strip()
    if not api_key:
        key_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api_key.txt')
        if os.path.exists(key_path):
            with open(key_path, 'r') as f:
                api_key = f.read().strip()
                
    if api_key:
        prompt = f"""
        Generate exactly 5 multiple-choice questions based on this course material.
        Return ONLY a JSON array, no markdown wrappers, no other text.
        Format:
        [
          {{
            "question": "Question text?",
            "A": "Option 1",
            "B": "Option 2",
            "C": "Option 3",
            "D": "Option 4",
            "correct": "A",
            "explanation": "Why A is correct."
          }}
        ]
        
        Course Context: {course_context}
        """
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]})
            req = urllib.request.Request(url, data=payload.encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                text = result['candidates'][0]['content']['parts'][0]['text']
                # Clean markdown JSON blocks if present
                if text.startswith('```json'):
                    text = text[7:]
                if text.startswith('```'):
                    text = text[3:]
                if text.endswith('```'):
                    text = text[:-3]
                return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API Quiz Gen Error: {e}")
            
    # Fallback to local topic-specific quiz if no API key or API fails
    return get_topic_fallback_quiz(course_context)

def get_topic_fallback_quiz(course_context):
    """
    Returns a highly relevant, 5-question multiple choice quiz
    based on the course name and current level number.
    Ensures students always get domain-relevant questions (Cloud, Programming, DB, etc.)
    """
    import re
    level_match = re.search(r'Level (\d+)', course_context)
    level_num = int(level_match.group(1)) if level_match else 1
    
    ctx = course_context.lower()
    
    # 1. Cloud Computing topic
    if any(k in ctx for k in ['cloud', 'aws', 'ec2', 'azure', 's3', 'virtualization']):
        if level_num == 1:
            return [
                {
                    "question": "What is the main definition of Cloud Computing?",
                    "A": "Processing data on a local hard drive",
                    "B": "On-demand delivery of IT resources over the internet with pay-as-you-go pricing",
                    "C": "Sending files via email",
                    "D": "Using physical copper cables to connect computers locally",
                    "correct": "B",
                    "explanation": "Cloud computing provides on-demand resources over the internet, eliminating local infrastructure requirements."
                },
                {
                    "question": "Which cloud service model is Google Docs / Gmail?",
                    "A": "IaaS (Infrastructure as a Service)",
                    "B": "PaaS (Platform as a Service)",
                    "C": "SaaS (Software as a Service)",
                    "D": "DaaS (Database as a Service)",
                    "correct": "C",
                    "explanation": "SaaS delivers fully functional end-user applications over the web."
                },
                {
                    "question": "What does IaaS stand for in cloud computing?",
                    "A": "Infrastructure as a Service",
                    "B": "Integration as a Service",
                    "C": "Internet as a Service",
                    "D": "Information as a Service",
                    "correct": "A",
                    "explanation": "IaaS provides virtualized computing resources, such as virtual machines, storage, and networks."
                },
                {
                    "question": "Which of the following is a key characteristic of cloud computing?",
                    "A": "Fixed capacity only",
                    "B": "High latency connections",
                    "C": "Rapid elasticity and on-demand self-service",
                    "D": "Manual server hardware patching by the customer",
                    "correct": "C",
                    "explanation": "Rapid elasticity allows scaling resources up and down quickly as demand changes."
                },
                {
                    "question": "What is a public cloud?",
                    "A": "Cloud infrastructure owned by a single private family",
                    "B": "Cloud services offered over the public internet and shared across multiple organizations",
                    "C": "A cloud server set up in a local school library",
                    "D": "Free cloud storage available for everyone globally",
                    "correct": "B",
                    "explanation": "Public cloud is owned by third-party providers and shared securely among multiple tenants."
                }
            ]
        elif level_num == 2:
            return [
                {
                    "question": "In cloud computing, what is AWS EC2 (Elastic Compute Cloud)?",
                    "A": "A cloud object storage service",
                    "B": "A virtual server (compute instance) in the cloud",
                    "C": "A relational database engine",
                    "D": "A content delivery network",
                    "correct": "B",
                    "explanation": "EC2 provides resizable virtual servers to run applications in AWS."
                },
                {
                    "question": "Which service is used for scalable flat object storage in AWS?",
                    "A": "AWS EC2",
                    "B": "AWS RDS",
                    "C": "AWS S3",
                    "D": "AWS VPC",
                    "correct": "C",
                    "explanation": "S3 (Simple Storage Service) is an object storage service offering high durability and scalability."
                },
                {
                    "question": "What type of storage is AWS EBS (Elastic Block Store)?",
                    "A": "Block storage for EC2 instances",
                    "B": "Object storage for static web assets",
                    "C": "File storage for local network sharing",
                    "D": "Archival storage for long-term backups",
                    "correct": "A",
                    "explanation": "EBS provides block-level storage volumes for use with EC2 instances."
                },
                {
                    "question": "What is the main difference between block storage and object storage?",
                    "A": "Block storage is slower than object storage",
                    "B": "Block storage is raw volumes for OS/Databases, while object storage is flat for files/media",
                    "C": "Object storage requires a partition table",
                    "D": "There is no difference",
                    "correct": "B",
                    "explanation": "Block storage behaves like raw hard drives; object storage stores data as flat objects with metadata."
                },
                {
                    "question": "What is an Availability Zone (AZ) in cloud architecture?",
                    "A": "A specific continent",
                    "B": "One or more discrete data centers with redundant power and networking in a Region",
                    "C": "A virtual private network",
                    "D": "A customer support timezone",
                    "correct": "B",
                    "explanation": "AZs are isolated locations within a Region designed to provide fault tolerance."
                }
            ]
        elif level_num == 3:
            return [
                {
                    "question": "What is a VPC (Virtual Private Cloud)?",
                    "A": "A public website host",
                    "B": "A logically isolated virtual network dedicated to your cloud account",
                    "C": "A private VPN software",
                    "D": "A physical server rack",
                    "correct": "B",
                    "explanation": "VPC lets you provision a private isolated section of the cloud to launch resources in."
                },
                {
                    "question": "What is a Security Group in cloud computing?",
                    "A": "A team of security guards",
                    "B": "A virtual firewall controlling inbound and outbound traffic for instances",
                    "C": "An encryption algorithm",
                    "D": "A user access list",
                    "correct": "B",
                    "explanation": "Security groups act as firewalls at the instance level."
                },
                {
                    "question": "What is the purpose of AWS IAM (Identity and Access Management)?",
                    "A": "To monitor server performance",
                    "B": "To securely control access to cloud resources and manage users/permissions",
                    "C": "To backup database tables",
                    "D": "To register domain names",
                    "correct": "B",
                    "explanation": "IAM enables you to manage access policies for users, groups, and roles."
                },
                {
                    "question": "Which component distributes incoming application traffic across multiple targets?",
                    "A": "NAT Gateway",
                    "B": "Route 53",
                    "C": "Elastic Load Balancer (ELB)",
                    "D": "Internet Gateway",
                    "correct": "C",
                    "explanation": "Load balancers distribute traffic across multiple target instances to improve reliability."
                },
                {
                    "question": "What is Route 53 in AWS?",
                    "A": "A database engine",
                    "B": "A highly available Domain Name System (DNS) web service",
                    "C": "A storage backup router",
                    "D": "A machine learning framework",
                    "correct": "B",
                    "explanation": "Route 53 is AWS's DNS service that maps domain names to IP addresses."
                }
            ]
        elif level_num == 4:
            return [
                {
                    "question": "What is the primary service for Relational Databases in AWS?",
                    "A": "AWS DynamoDB",
                    "B": "AWS RDS (Relational Database Service)",
                    "C": "AWS Redshift",
                    "D": "AWS ElastiCache",
                    "correct": "B",
                    "explanation": "RDS makes it easy to set up, operate, and scale relational databases (MySQL, PostgreSQL, etc.) in the cloud."
                },
                {
                    "question": "Which database model best describes AWS DynamoDB?",
                    "A": "Relational Database",
                    "B": "Graph Database",
                    "C": "NoSQL Key-Value Database",
                    "D": "File-based Database",
                    "correct": "C",
                    "explanation": "DynamoDB is a fully managed, fast, and flexible NoSQL database service."
                },
                {
                    "question": "What is Horizontal Scaling (Scaling Out) in cloud architecture?",
                    "A": "Adding more RAM or CPU to an existing server",
                    "B": "Adding more instances/servers to a resource pool",
                    "C": "Moving servers to a different country",
                    "D": "Switching from public to private cloud",
                    "correct": "B",
                    "explanation": "Horizontal scaling adds more nodes/machines to distribute the load."
                },
                {
                    "question": "What is the purpose of Auto-Scaling in the cloud?",
                    "A": "To automatically write code",
                    "B": "To dynamically adjust resources (add/remove instances) based on current load",
                    "C": "To change database passwords automatically",
                    "D": "To schedule automatic backups",
                    "correct": "B",
                    "explanation": "Auto-scaling ensures you have the right number of instances to handle your traffic, saving costs."
                },
                {
                    "question": "What is Serverless Computing (e.g., AWS Lambda)?",
                    "A": "Computing without any servers existing in the world",
                    "B": "Code execution where the cloud provider fully manages server provisioning and scaling",
                    "C": "Running code on a local router",
                    "D": "Computing using offline files",
                    "correct": "B",
                    "explanation": "In serverless, the cloud provider manages infrastructure; you only pay for the exact execution time."
                }
            ]
        else: # level 5
            return [
                {
                    "question": "What is a Content Delivery Network (CDN) like AWS CloudFront used for?",
                    "A": "Compiling server-side code",
                    "B": "Caching and delivering web content globally with low latency via edge locations",
                    "C": "Compressing database tables",
                    "D": "Setting up user permissions",
                    "correct": "B",
                    "explanation": "CDNs store static assets closer to users at edge locations to speed up loading."
                },
                {
                    "question": "What is Infrastructure as Code (IaC)?",
                    "A": "Writing code using servers",
                    "B": "Managing and provisioning cloud infrastructure using machine-readable configuration files",
                    "C": "Building physical server racks by hand",
                    "D": "Writing standard application code",
                    "correct": "B",
                    "explanation": "IaC tools (e.g., Terraform, CloudFormation) let you deploy infrastructure programmatically."
                },
                {
                    "question": "What does the term 'Multi-Tenancy' mean in cloud computing?",
                    "A": "A single server owned by one tenant",
                    "B": "Multiple tenants/customers sharing the same underlying hardware resources securely",
                    "C": "Rent data centers to different governments",
                    "D": "Run multiple OS on a local PC",
                    "correct": "B",
                    "explanation": "Multi-tenancy is the shared resource model that makes cloud computing cost-effective."
                },
                {
                    "question": "What is the main benefit of Containerization (e.g., Docker) over traditional VMs?",
                    "A": "Containers include their own full OS kernel",
                    "B": "Containers are highly portable, lightweight, and share the host OS kernel",
                    "C": "Containers do not run on servers",
                    "D": "Containers are completely immune to security threats",
                    "correct": "B",
                    "explanation": "Containers are fast and lightweight because they share the host OS kernel instead of virtualizing hardware."
                },
                {
                    "question": "Which AWS service is used for resource monitoring, alerts, and log analysis?",
                    "A": "AWS Config",
                    "B": "AWS CloudWatch",
                    "C": "AWS CloudTrail",
                    "D": "AWS Inspector",
                    "correct": "B",
                    "explanation": "CloudWatch monitors performance metrics, tracks logs, and sets alarms."
                }
            ]
            
    # 2. Programming / Python / Java
    elif any(k in ctx for k in ['python', 'programming', 'code', 'java', 'oop', 'language']):
        if level_num == 1:
            return [
                {
                    "question": "What is Python?",
                    "A": "A low-level assembly language",
                    "B": "A high-level, interpreted programming language",
                    "C": "A hardware database router",
                    "D": "An operating system",
                    "correct": "B",
                    "explanation": "Python is known for its clean syntax and readability as an interpreted language."
                },
                {
                    "question": "Which of the following is a mutable data type in Python?",
                    "A": "Tuple",
                    "B": "String",
                    "C": "List",
                    "D": "Integer",
                    "correct": "C",
                    "explanation": "Lists can be modified after creation, unlike tuples, strings, and integers."
                },
                {
                    "question": "How do you start a single-line comment in Python?",
                    "A": "// This is a comment",
                    "B": "/* This is a comment */",
                    "C": "# This is a comment",
                    "D": "<!-- This is a comment -->",
                    "correct": "C",
                    "explanation": "The hash (#) character is used to denote comments in Python."
                },
                {
                    "question": "What is the output of len([1, 2, 3]) in Python?",
                    "A": "1",
                    "B": "2",
                    "C": "3",
                    "D": "Error",
                    "correct": "C",
                    "explanation": "The len() function returns the number of items in a sequence."
                },
                {
                    "question": "Which function is used to print output to the console in Python?",
                    "A": "console.log()",
                    "B": "print()",
                    "C": "System.out.println()",
                    "D": "echo()",
                    "correct": "B",
                    "explanation": "The print() function outputs strings or data to the terminal in Python."
                }
            ]
        else:
            return [
                {
                    "question": "What keyword is used to define a function in Python?",
                    "A": "function",
                    "B": "def",
                    "C": "func",
                    "D": "define",
                    "correct": "B",
                    "explanation": "The 'def' keyword starts a function definition block in Python."
                },
                {
                    "question": "How does Python determine code blocks (loops, conditionals)?",
                    "A": "Curly braces {}",
                    "B": "Semicolons ;",
                    "C": "Indentation (whitespace)",
                    "D": "Parentheses ()",
                    "correct": "C",
                    "explanation": "Python uses indentation levels instead of braces to define blocks of code."
                },
                {
                    "question": "What is self in a Python class method?",
                    "A": "A keyword representing a static method",
                    "B": "A reference to the current instance of the class",
                    "C": "A global variable",
                    "D": "A constructor function",
                    "correct": "B",
                    "explanation": "Self is used to access attributes and methods associated with the specific object instance."
                },
                {
                    "question": "What is the constructor method in a Python class?",
                    "A": "def constructor(self):",
                    "B": "def init(self):",
                    "C": "def __init__(self):",
                    "D": "def __new__(self):",
                    "correct": "C",
                    "explanation": "The __init__ method is automatically called when an object is instantiated."
                },
                {
                    "question": "What is inheritance in Object-Oriented Programming?",
                    "A": "Creating multiple objects of the same class",
                    "B": "A child class deriving attributes and behaviors from a parent class",
                    "C": "Hiding internal data details",
                    "D": "Overloading operators",
                    "correct": "B",
                    "explanation": "Inheritance allows code reuse by building specialized classes based on base classes."
                }
            ]

    # 3. Database / SQL
    elif any(k in ctx for k in ['database', 'sql', 'mysql', 'dbms', 'rdbms']):
        return [
            {
                "question": "What does SQL stand for?",
                "A": "Structured Query Language",
                "B": "Simple Question Language",
                "C": "System Query Logic",
                "D": "Sequential Query List",
                "correct": "A",
                "explanation": "SQL is the standard language for managing relational databases."
            },
            {
                "question": "Which SQL constraint uniquely identifies each record in a database table?",
                "A": "FOREIGN KEY",
                "B": "UNIQUE KEY",
                "C": "PRIMARY KEY",
                "D": "NOT NULL",
                "correct": "C",
                "explanation": "A PRIMARY KEY constraint uniquely identifies each row and must contain unique, non-null values."
            },
            {
                "question": "Which SQL statement is used to fetch data from a database?",
                "A": "GET",
                "B": "SELECT",
                "C": "EXTRACT",
                "D": "READ",
                "correct": "B",
                "explanation": "The SELECT statement is used to query database records."
            },
            {
                "question": "What type of JOIN returns records that have matching values in both tables?",
                "A": "LEFT JOIN",
                "B": "RIGHT JOIN",
                "C": "INNER JOIN",
                "D": "OUTER JOIN",
                "correct": "C",
                "explanation": "INNER JOIN returns rows only when there is a match in both joined tables."
            },
            {
                "question": "What is the purpose of the SQL WHERE clause?",
                "A": "To specify which table to select from",
                "B": "To filter records that satisfy a specific condition",
                "C": "To sort the output results",
                "D": "To group data by column",
                "correct": "B",
                "explanation": "The WHERE clause is used to filter records based on boolean conditions."
            }
        ]

    # Default / General IT Fallback
    return [
        {
            "question": "What does CPU stand for?",
            "A": "Central Processing Unit",
            "B": "Computer Personal Unit",
            "C": "Central Process Utility",
            "D": "Control Power Unit",
            "correct": "A",
            "explanation": "The CPU is the primary component of a computer that acts as its brain."
        },
        {
            "question": "Which of the following is a volatile memory?",
            "A": "ROM",
            "B": "RAM",
            "C": "Hard Drive",
            "D": "Flash Drive",
            "correct": "B",
            "explanation": "RAM is volatile; it loses its content when the computer is powered off."
        },
        {
            "question": "What is the primary function of an Operating System (OS)?",
            "A": "To browse the web",
            "B": "To manage computer hardware and software resources",
            "C": "To compile application code",
            "D": "To protect against all internet viruses",
            "correct": "B",
            "explanation": "The OS acts as an intermediary between users and computer hardware."
        },
        {
            "question": "Which protocol is primarily used to secure web browser communications?",
            "A": "HTTP",
            "B": "HTTPS",
            "C": "FTP",
            "D": "SMTP",
            "correct": "B",
            "explanation": "HTTPS encrypts communications between the browser and web server using SSL/TLS."
        },
        {
            "question": "What does IP stand for in IP Address?",
            "A": "Internet Protocol",
            "B": "Intranet Page",
            "C": "Instant Packet",
            "D": "Information Path",
            "correct": "A",
            "explanation": "IP is the set of rules governing the format of data sent over the internet or local network."
        }
    ]

