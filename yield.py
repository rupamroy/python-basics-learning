
students = []
def read_file():
    try:
        f=open("students.txt","r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception as error:
        print("could not read file \n" + error)

# This is our version of readline for which we need to use the yield function
def read_students(f):
    for line in f:
        yield line

read_file()
print(students)