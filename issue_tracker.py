from sqlite3 import connect


def initialize_database():
    connection = connect("issue_tracker.db")
    sql = """CREATE TABLE IF NOT EXISTS issue (
        issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        due_date DATE,
        priority INTEGER
    );"""

    cursor = connection.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()


def add_issue(name, description, due_date, priority):
    connection = connect("issue_tracker.db")

    sql = f"INSERT INTO issue (name, description, due_date, priority) VALUES ('{name}', '{description}', '{due_date}', {priority});"

    cursor = connection.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()


def get_issues():
    connection = connect("issue_tracker.db")
    cursor = connection.execute("SELECT * FROM issue;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data