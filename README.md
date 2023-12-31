# COMP 3005A Winter 2023
### Assignment 4
### Erica Li 

## How to run:
1. In postgreSQL, initialize a new database called "Students". Leave it blank.
2. Change the configuration variables in vars.py to your local pgadmin values. You will probably just need to change the password to whatever your user's password is.
3. Run `pip install psycopg2` in your terminal to install the libraries. If that doesn't work, then try `pip install psycopg2-binary==2.9.1`
4. Run `python3 server.py` to start the program. You can now use the CRUD operations through the command line interface of the program.
## Application functions:
- getAllStudents(): Retrieves and displays all records from the students table.
- addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
- updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
- deleteStudent(student_id): Deletes the record of the student with the specified student_id.

## Video:
- https://youtu.be/XBgc1kIArmw
