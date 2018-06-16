students = []

def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase=get_students_titlecase()
    print(students_titlecase)

# function with optional parameter
def add_student(name, student_id=332):
    student = {
        "name": name,
        "student_id": student_id
    }
    students.append(student)

def save_file(student):
    try:
        f = open("students.txt", "a")
        # w - writing overrides entire file
        # r - reading a text file
        # a - appending to a new or existing file
        # rb - reading a binary file
        # wb - writing to a binary file
        f.write(student + "\n")
        f.close() # close is must to prevent file locking issues 
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f=open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as error:
        print("could not read file \n" + error)


read_file()
print_students_titlecase()

addStudent = True
while(addStudent == True):
    student_name = input("Enter student name: ")
    student_id = input("Enter student Id: ")
    add_student(student_name, student_id)
    save_file(student_name)
    addstudent=input('Do you want to add more student y/n: ')
    if(addstudent != 'y'):
        addStudent = False

print_students_titlecase()


