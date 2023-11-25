import psycopg2
from datetime import datetime
from vars import hostname, database, username, pwd, port_id
conn = None
cursor = None

# Retrieves and displays all records from the students table
def getAllStudents():
    return 'SELECT * FROM students;'

# Inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    first_name = "'" + first_name + "'"
    last_name = "'" + last_name + "'"
    email = "'" + email + "'"
    enrollment_date = "'" + enrollment_date + "'"
    return 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (' + first_name + ', ' + last_name + ', ' + email + ', ' + enrollment_date + ');'

# Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    new_email = "'" + new_email + "'"
    return 'UPDATE students SET email = ' + new_email + ' WHERE id = ' + str(student_id) + ';' 

# Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    return 'DELETE FROM students WHERE id = ' + str(student_id) + ';'

try:
    # Connecting to the database in pgadmin
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    # Creating a cursor 
    cursor = conn.cursor()
    # Initialzing table and columns in database
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
    # Insert initial data in table
    insert_script = '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');'''
    cursor.execute(insert_script)
    # Main logic execution loop
    while True:
        conn.commit()
        selection = input("Enter A to add a new student \n Enter G to get all students \n Enter U to update an email \n Enter D to delete an entry \n Enter any other key to quit: ")
        if selection == 'A':
            newFN = input("Enter the new student's first name: ")
            newLN = input("Enter the new student's last name: ")
            proceed = False
            # Validation for email input
            while proceed == False:
                newEmail = input("Enter the new student's email: ")
                cursor.execute("SELECT email FROM students WHERE email='" + newEmail + "'")
                students = cursor.fetchall()
                if not students:
                    proceed = True
                else:
                    print("Student with this email already exists, please try again: ")
            proceed = False
            # Validation for date input
            while proceed == False:
                newDate = input("Enter the new student's enrollment date (must be formatted as YYYY-MM-DD): ")
                try:
                    proceed = bool(datetime.strptime(newDate, "%Y-%m-%d"))
                except ValueError:
                    print("Date was not formatted correctly, please try again: ")
            print("Adding New Student... \n")
            cursor.execute(addStudent(newFN, newLN, newEmail, newDate))
        elif selection == 'G':
            print("Getting all students...")
            cursor.execute(getAllStudents())
            for entry in cursor.fetchall():
                print(entry)
        elif selection == 'U':
            proceed = False
            # Validation for id input
            while proceed == False:
                id = input("Enter the student ID of the student you wish to update: ")
                cursor.execute("SELECT id FROM students WHERE id = " + id + ";")
                ids = cursor.fetchall()
                if ids:
                    proceed = True
                else:
                    print("Student with the entered ID does not exist, please try again: ")
            proceed = False
            # Validation for email input
            while proceed == False:
                email = input("Enter the new student's email: ")
                cursor.execute("SELECT email FROM students WHERE email='" + email + "'")
                students = cursor.fetchall()
                if not students:
                    proceed = True
                else:
                    print("Student with this email already exists, please try again: ")
            
            print("Updating email...")
            cursor.execute(updateStudentEmail(id, email))
        elif selection == 'D':
            proceed = False
            # Validation for email input
            while proceed == False:
                id = input("Enter the student ID of the student you wish to delete: ")
                cursor.execute("SELECT id FROM students WHERE id = " + id + ";")
                students = cursor.fetchall()
                if students:
                    proceed = True
                else:
                    print("Student with id does not exist, please try again: ")
            cursor.execute(deleteStudent(id))
        else:
            print("Terminating the program...")
            break
    
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
   
