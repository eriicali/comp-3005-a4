import psycopg2

hostname = 'localhost'
database = 'Students'
username = 'postgres'
pwd = 'admin123'
port_id = 5432
conn = None
#cursor = None

def getAllStudents():
    return 'SELECT * FROM students;'
    
def addStudent(first_name, last_name, email, enrollment_date):
    
    pass
def updateStudentEmail(student_id, new_email):
    pass
def deleteStudent(student_id):
    pass


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS students')
    init_db = ''' CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        enrollment_date DATE
        );
    ''' 
    cursor.execute(init_db)
    insert_script = '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');'''
    cursor.execute(insert_script)
    cursor.execute(getAllStudents())
    print(cursor.fetchall())
    print("line 48")
    conn.commit()
    
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
   
